import datetime
import re
from typing import Optional

from PySide6.QtCore import Qt, QDate, QTimer, QObject, Signal, QThread
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QMessageBox, QApplication
from PySide6.QtGui import QSyntaxHighlighter, QTextCharFormat
from PySide6.QtWidgets import QVBoxLayout, QCalendarWidget, QLabel
from requests import ConnectTimeout, ReadTimeout, Timeout
from urllib3 import request

from .component.analog_clock import AnalogClock
from .component.digital_clock import DigitalClock
from .ui.tool_widget import Ui_ToolWidget
from app import util
from app.util import time as timeutil, json_pretty
from app.service.request import Request, RequestMethod, Response, RequestSettings
from app.service.logger import LOGGER
from .worker.request import RequestProgressEvent, RequestFinishEvent, RequestWorkerThread


class ToolWidget(QWidget):
    def __init__(self):
        super(ToolWidget, self).__init__()
        self.ui = Ui_ToolWidget()
        self.ui.setupUi(self)

        # request
        self._request_worker: Optional[RequestWorkerThread] = None

        # init actions and widget
        self._init_actions()
        self._init_widget()

    def _init_actions(self):
        # time
        self.ui.currentTimeButton.clicked.connect(self.show_current_time)
        self.ui.timestampConvertButton.clicked.connect(self.convert_timestamp)
        self.ui.timestrConvertButton.clicked.connect(self.convert_timestr)

        # json
        self.ui.jsonFormatButton.clicked.connect(self.format_json)
        self.ui.jsonToYamlButton.clicked.connect(self.json_to_yaml)
        self.ui.jsonFromYamlButton.clicked.connect(self.json_from_yaml)
        self.ui.jsonResultCopyButton.clicked.connect(self.copy_json_result)

        # request
        self.ui.requestInvokeButton.clicked.connect(self.invoke_request)
        self.ui.requestExportCurlButton.clicked.connect(self.export_request_curl)
        self.ui.requestHeadersResetButton.clicked.connect(self.reset_request_headers)
        self.ui.requestHeadersAddButton.clicked.connect(self.add_request_header)
        self.ui.requestHeadersRemoveButton.clicked.connect(self.remove_request_header)


    def _init_widget(self):
        # calendar
        self._timerCalendar = QTimer(self)
        self._timerCalendar.timeout.connect(self._ensure_current_date)
        self._timerCalendar.start(100)

        # individual clocks：AnalogClock + DigitalClock + 当前时间戳
        self._timeClockLayout = QVBoxLayout(self.ui.timeClockWidget)
        self._timeClockLayout.setContentsMargins(12, 0, 12, 0)
        self.timeAnalogClock = AnalogClock(self.ui.timeClockWidget)
        self.timeAnalogClock.setFixedSize(200, 200)
        self._timeClockLayout.addWidget(self.timeAnalogClock)
        self.timeDigitalClock = DigitalClock(self.ui.timeClockWidget)
        self.timeDigitalClock.setFixedSize(200, 50)
        self._timeClockLayout.addWidget(self.timeDigitalClock)

        # set clocks to current time
        self.show_current_time()  # set current date here

        # json
        self.ui.jsonFormatIndentComboBox.setCurrentText("4")  # default indent is 4

        # request
        default_request = Request()
        self.ui.requestMethodComboBox.setCurrentText(default_request.method)

        # request headers
        self.reset_request_headers()

        # request settings
        default_request_settings = default_request.settings
        self.ui.requestSettingsConnectTimeoutLineEdit.setText(str(default_request_settings.connect_timeout))
        self.ui.requestSettingsReadTimeoutLineEdit.setText(str(default_request_settings.read_timeout))

    def _get_time_precision(self):
        precision_type = self.ui.timeSettingsPrecisionComboBox.currentText()
        if precision_type == '毫秒':
            return timeutil.Precision.MILLISECOND
        elif precision_type == '秒':
            return timeutil.Precision.SECOND
        else:
            return timeutil.Precision.UNKNOWN

    def _get_time_format(self):
        format_type = ''
        format_type_lower = self.ui.timeSettingsFormatComboBox.currentText().lower()
        if format_type_lower.startswith('默认'):
            format_type = 'default'
        elif format_type_lower.startswith('rfc3339'):
            format_type = 'rfc3339'

        if format_type == '':
            return self.ui.timeSettingsCustomFormatLineEdit.text()

        precision = self._get_time_precision()
        return timeutil.get_format(precision, format_type)

    def _set_current_date(self):
        self.ui.timeCalendarWidget.setSelectedDate(QDate.currentDate())

    def _ensure_current_date(self):
        if self.ui.timeCalendarWidget.selectedDate() != QDate.currentDate():
            self._set_current_date()

    def show_current_time(self):
        now = datetime.datetime.now()

        # time string
        time_format = self._get_time_format()
        if time_format == '':
            self.ui.currentTimeStringLineEdit.setText('不支持当前格式')
        else:
            s, e = timeutil.to_string(now, time_format)
            if e is not None:
                self.ui.currentTimeStringLineEdit.setText(f'转换失败：{e}')
            else:
                self.ui.currentTimeStringLineEdit.setText(s)

        # timestamp
        precision = self._get_time_precision()
        timestamp, e = timeutil.to_timestamp(now, precision)
        if e is not None:
            self.ui.currentTimeStampLineEdit.setText(f'转换失败：{e}')
        else:
            self.ui.currentTimeStampLineEdit.setText(f'{timestamp}')

        # set calendar
        self._set_current_date()

    def convert_timestamp(self):
        timestamp_str = self.ui.timestampLineEdit.text().strip()
        if not timestamp_str:
            self.ui.timestampConvertResultLineEdit.setText('未输入时间戳')
            return
        try:
            timestamp = int(timestamp_str)
        except Exception as e:
            self.ui.timestampConvertResultLineEdit.setText(f'时间戳输入不正确：{e}')
            return

        # parse as time
        precision = self._get_time_precision()
        tm, e = timeutil.from_timestamp(timestamp, precision)
        if e is not None:
            self.ui.timestampConvertResultLineEdit.setText(f'解析失败：{e}')
            return

        # convert to string
        fmt = self._get_time_format()
        if fmt == '':
            self.ui.timestampConvertResultLineEdit.setText(f'不支持当前转换格式')
            return
        s, e = timeutil.to_string(tm, fmt)
        if e is not None:
            self.ui.timestampConvertResultLineEdit.setText(f'转换失败：{e}')
        else:
            self.ui.timestampConvertResultLineEdit.setText(s)

    def convert_timestr(self):
        timestr = self.ui.timestrLineEdit.text().strip()
        if not timestr:
            self.ui.timestrConvertResultLineEdit.setText('未输入时间字符串')
            return

        # try format as seconds/milliseconds
        fmt = self._get_time_format()
        if fmt == '':
            self.ui.timestrConvertResultLineEdit.setText('不支持当前解析格式')
            return
        tm, e = timeutil.from_string(timestr, fmt)
        if e is not None:
            self.ui.timestrConvertResultLineEdit.setText(f'解析失败：{e}')
            return

        # convert to timestamp
        precision = self._get_time_precision()
        timestamp, e = timeutil.to_timestamp(tm, precision)
        if e is not None:
            self.ui.timestrConvertResultLineEdit.setText(f'转换失败：{e}')
        else:
            self.ui.timestrConvertResultLineEdit.setText(f'{timestamp}')

    def _get_json_indent(self):
        indent_text = self.ui.jsonFormatIndentComboBox.currentText()
        try:
            indent = int(indent_text)
        except:
            indent = None
        if indent is not None:
            if indent <= 0:
                indent = None
            elif indent > 8:
                indent = 8
        return indent


    def format_json(self):
        content = self.ui.jsonTextEdit.toPlainText()
        obj, e = util.json_load(content)
        if e is not None:
            self.ui.jsonResultTextEdit.setText(f'解析JSON失败：{e}')
            return

        indent = self._get_json_indent()
        format_content, e = util.json_dump(obj, indent=indent, ensure_ascii=False)
        if e is not None:
            self.ui.jsonResultTextEdit.setText(f'格式化JSON失败：{e}')
        else:
            self.ui.jsonResultTextEdit.setText(f'{format_content}')

    def json_to_yaml(self):
        content = self.ui.jsonTextEdit.toPlainText()
        obj, e = util.json_load(content)
        if e is not None:
            self.ui.jsonResultTextEdit.setText(f'解析JSON失败：{e}')
            return

        indent = self._get_json_indent()
        format_content, e = util.yaml_dump(obj, indent=indent, allow_unicode=True)
        if e is not None:
            self.ui.jsonResultTextEdit.setText(f'JSON转YAML失败：{e}')
        else:
            self.ui.jsonResultTextEdit.setText(f'{format_content}')

    def json_from_yaml(self):
        content = self.ui.jsonTextEdit.toPlainText()
        obj, e = util.yaml_load(content)
        if e is not None:
            self.ui.jsonResultTextEdit.setText(f'解析YAML失败：{e}')
            return

        indent = self._get_json_indent()
        format_content, e = util.json_dump(obj, indent=indent, ensure_ascii=False)
        if e is not None:
            self.ui.jsonResultTextEdit.setText(f'YAML转JSON失败：{e}')
        else:
            self.ui.jsonResultTextEdit.setText(f'{format_content}')

    def copy_json_result(self):
        result_text = self.ui.jsonResultTextEdit.toPlainText()
        if not result_text:
            return
        self.ui.jsonResultTextEdit.selectAll()
        self.ui.jsonResultTextEdit.copy()

    def _set_request_headers(self, headers):
        if not isinstance(headers, dict):
            self.ui.requestHeadersTableWidget.setRowCount(0)
            return
        self.ui.requestHeadersTableWidget.setRowCount(len(headers))
        r = 0
        for k in sorted(headers.keys()):
            v = headers[k]
            self.ui.requestHeadersTableWidget.setItem(r, 0, QTableWidgetItem(k))
            self.ui.requestHeadersTableWidget.setItem(r, 1, QTableWidgetItem(v))
            r += 1

    def reset_request_headers(self):
        req = Request()
        self._set_request_headers(req.headers)

    def add_request_header(self):
        row_count = self.ui.requestHeadersTableWidget.rowCount()
        self.ui.requestHeadersTableWidget.setRowCount(row_count + 1)

    def remove_request_header(self):
        row = -1
        items = self.ui.requestHeadersTableWidget.selectedItems()
        for item in items:
            row = item.row()
            break
        if row >= 0:
            self.ui.requestHeadersTableWidget.removeRow(row)

    def _set_request_status(self, status: str):
        self.ui.requestStatusLabel.setText(f'状态：{status}')

    def _set_request_duration(self, seconds: float):
        self.ui.requestDurationLabel.setText(f'用时：{seconds:.3f}s')

    def on_request_start(self, _):
        LOGGER.debug(f'request start')
        self.ui.requestInvokeButton.setEnabled(False)
        self._set_request_status('执行中')
        self._set_request_duration(0)

    def on_request_progress(self, evt: RequestProgressEvent):
        LOGGER.debug(f'request progress -> seconds: {evt.seconds}')
        self._set_request_duration(evt.seconds)

    def _gen_resp_detail(self, evt: RequestFinishEvent):
        lines = []
        # indent = ' ' * 2

        # request
        lines.append(f'{"=" * 20} 请求数据 {"=" * 20}')
        if evt.req is None:
            lines.append('无')
        else:
            lines.append(f'Method: {evt.req.method}')
            lines.append(f'URL: {evt.req.url}')
            lines.append(f'Settings: {str(evt.req.settings)}')
            lines.append(''),
            lines.append(f'{"-" * 15} Headers ({len(evt.req.headers)}) {"-" * 15}'),
            for k, v in evt.req.headers.items():
                lines.append(f'{k}: {v}')
            lines.append(''),
            lines.append(f'{"-" * 15} Body ({len(evt.req.body)}) {"-" * 15}')
            lines.append(str(evt.req.body))
        lines.append('\n')

        # response
        lines.append(f'{"=" * 20} 返回数据 {"=" * 20}')
        if evt.resp is None:
            lines.append('无')
        else:
            lines.append(f'Status Code：{evt.resp.status_code}')
            lines.append(''),
            lines.append(f'{"-" * 15} Headers ({len(evt.resp.headers)}) {"-" * 15}'),
            for k, v in evt.resp.headers.items():
                lines.append(f'{k}: {v}')
            lines.append(''),
            lines.append(f'{"-" * 15} Body ({len(evt.resp.body)}) {"-" * 15}')
            lines.append(str(evt.resp.body))
        lines.append('\n')

        # err
        lines.append(f'{"=" * 20} 异常信息 {"=" * 20}')
        if evt.err is None:
            lines.append('无')
        else:
            lines.append(str(evt.err))

        return '\n'.join(lines)

    def on_request_finish(self, evt: RequestFinishEvent):
        LOGGER.debug(f'request finish -> resp: {str(evt.resp)}, err: {evt.err}')

        # set resp status
        if evt.resp is None:
            if evt.err is None:
                self._set_request_status('无响应')
            else:
                if isinstance(evt.err, (Timeout, ConnectTimeout, ReadTimeout)):
                    self._set_request_status('请求超时')
                else:
                    self._set_request_status('请求异常')
        else:
            status_code = evt.resp.status_code
            if 200 <= status_code < 300:
                self._set_request_status(f'{status_code} 成功')
            elif 300 <= status_code < 400:
                self._set_request_status(f'{status_code} 重定向')
            elif 400 <= status_code < 500:
                self._set_request_status(f'{status_code} 客户端错误')
            elif 500 <= status_code < 600:
                self._set_request_status(f'{status_code} 服务器错误')
            else:
                self._set_request_status(f'{status_code} 未知')

        # set resp duration
        self._set_request_duration(evt.seconds)

        # set resp body
        if evt.resp is None:
            self.ui.requestRespBodyTextEdit.clear()
        else:
            body = json_pretty(evt.resp.body)
            self.ui.requestRespBodyTextEdit.setText(body)

        # set resp headers
        if evt.resp is None:
            self.ui.requestRespHeadersTableWidget.setRowCount(0)
        else:
            headers = evt.resp.headers
            headers_size = len(headers.keys())
            self.ui.requestRespHeadersTableWidget.setRowCount(headers_size)
            r = 0
            for k in sorted(headers.keys()):
                v = headers[k]
                self.ui.requestRespHeadersTableWidget.setItem(r, 0, QTableWidgetItem(k))
                self.ui.requestRespHeadersTableWidget.setItem(r, 1, QTableWidgetItem(v))
                r += 1

        # set resp detail
        detail = self._gen_resp_detail(evt)
        self.ui.requestRespDetailTextEdit.setText(detail)

        # clear all states
        if self._request_worker:
            self._request_worker.quit()
            self._request_worker.wait()
            self._request_worker.deleteLater()
            self._request_worker = None
        self.ui.requestInvokeButton.setEnabled(True)

    def _reset_request_state(self):
        """clear all previous request states"""
        if self._request_worker is not None:
            self._request_worker.quit()
            self._request_worker.wait()
            self._request_worker.deleteLater()
            self._request_worker = None

        self.ui.requestRespBodyTextEdit.clear()
        self.ui.requestRespHeadersTableWidget.setRowCount(0)
        self.ui.requestRespDetailTextEdit.clear()

    def _gen_request(self) -> Request:
        # load headers
        headers = {}
        for r in range(self.ui.requestHeadersTableWidget.rowCount()):
            k = self.ui.requestHeadersTableWidget.item(r, 0).text().strip()
            v = self.ui.requestHeadersTableWidget.item(r, 1).text().strip()
            if k and v:
                headers[k] = v

        # load settings
        settings = RequestSettings()
        try:
            settings.connect_timeout = int(self.ui.requestSettingsConnectTimeoutLineEdit.text())
        except Exception:
            pass
        try:
            settings.read_timeout = int(self.ui.requestSettingsReadTimeoutLineEdit.text())
        except Exception:
            pass

        # generate request
        req = Request(
            method=self.ui.requestMethodComboBox.currentText(),
            url = self.ui.requestUrlLineEdit.text(),
            headers=headers,
            body=self.ui.requestReqBodyTextEdit.toPlainText().strip(),
            settings=settings
        )
        return req

    def invoke_request(self):
        LOGGER.debug('invoke request -> triggered')
        if self._request_worker is not None and self._request_worker.isRunning():
            LOGGER.warning(f'cannot invoke request, request worker is active')
            return
        self._reset_request_state()
        req = self._gen_request()
        LOGGER.debug(f'invoke request -> req: {req.args()}')
        self._request_worker = RequestWorkerThread(req, parent=self)
        self._request_worker.signals.start.connect(self.on_request_start)
        self._request_worker.signals.progress.connect(self.on_request_progress)
        self._request_worker.signals.finish.connect(self.on_request_finish)
        self._request_worker.start(priority=QThread.Priority.LowPriority)
        LOGGER.debug(f'invoke request -> thread started')

    def export_request_curl(self):
        req = self._gen_request()
        curl, err = req.to_curl()
        if err is not None:
            QMessageBox.critical(self, '导出CURL', f'导出CURL失败！错误信息：{err}')
        else:
            clipboard = QApplication.clipboard()
            clipboard.setText(curl)
            QMessageBox.information(self, '导出CURL', f'导出CURL成功，已复制到剪贴板！')
