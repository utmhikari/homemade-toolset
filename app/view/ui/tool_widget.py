# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tool_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCalendarWidget, QComboBox,
    QFormLayout, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTabWidget, QTableWidget, QTableWidgetItem,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_ToolWidget(object):
    def setupUi(self, ToolWidget):
        if not ToolWidget.objectName():
            ToolWidget.setObjectName(u"ToolWidget")
        ToolWidget.resize(960, 720)
        self.gridLayout_4 = QGridLayout(ToolWidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.tabWidget = QTabWidget(ToolWidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.timeWidget = QWidget()
        self.timeWidget.setObjectName(u"timeWidget")
        self.verticalLayout = QVBoxLayout(self.timeWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.timeHeaderWidget = QWidget(self.timeWidget)
        self.timeHeaderWidget.setObjectName(u"timeHeaderWidget")
        self.timeHeaderLayout = QHBoxLayout(self.timeHeaderWidget)
        self.timeHeaderLayout.setObjectName(u"timeHeaderLayout")
        self.timeHeaderLayout.setContentsMargins(0, 0, 0, 0)
        self.timeCalendarWidget = QCalendarWidget(self.timeHeaderWidget)
        self.timeCalendarWidget.setObjectName(u"timeCalendarWidget")
        self.timeCalendarWidget.setAutoFillBackground(True)
        self.timeCalendarWidget.setGridVisible(True)
        self.timeCalendarWidget.setSelectionMode(QCalendarWidget.SelectionMode.NoSelection)
        self.timeCalendarWidget.setHorizontalHeaderFormat(QCalendarWidget.HorizontalHeaderFormat.LongDayNames)
        self.timeCalendarWidget.setVerticalHeaderFormat(QCalendarWidget.VerticalHeaderFormat.NoVerticalHeader)
        self.timeCalendarWidget.setNavigationBarVisible(True)
        self.timeCalendarWidget.setDateEditEnabled(False)

        self.timeHeaderLayout.addWidget(self.timeCalendarWidget)

        self.timeClockWidget = QWidget(self.timeHeaderWidget)
        self.timeClockWidget.setObjectName(u"timeClockWidget")

        self.timeHeaderLayout.addWidget(self.timeClockWidget)


        self.verticalLayout.addWidget(self.timeHeaderWidget)

        self.timeSettingsWidget = QWidget(self.timeWidget)
        self.timeSettingsWidget.setObjectName(u"timeSettingsWidget")
        self.horizontalLayout_7 = QHBoxLayout(self.timeSettingsWidget)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.timeSettingsPrecisionLabel = QLabel(self.timeSettingsWidget)
        self.timeSettingsPrecisionLabel.setObjectName(u"timeSettingsPrecisionLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timeSettingsPrecisionLabel.sizePolicy().hasHeightForWidth())
        self.timeSettingsPrecisionLabel.setSizePolicy(sizePolicy)

        self.horizontalLayout_7.addWidget(self.timeSettingsPrecisionLabel)

        self.timeSettingsPrecisionComboBox = QComboBox(self.timeSettingsWidget)
        self.timeSettingsPrecisionComboBox.addItem("")
        self.timeSettingsPrecisionComboBox.addItem("")
        self.timeSettingsPrecisionComboBox.setObjectName(u"timeSettingsPrecisionComboBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.timeSettingsPrecisionComboBox.sizePolicy().hasHeightForWidth())
        self.timeSettingsPrecisionComboBox.setSizePolicy(sizePolicy1)

        self.horizontalLayout_7.addWidget(self.timeSettingsPrecisionComboBox)

        self.timeSettingsFormatLabel = QLabel(self.timeSettingsWidget)
        self.timeSettingsFormatLabel.setObjectName(u"timeSettingsFormatLabel")
        sizePolicy.setHeightForWidth(self.timeSettingsFormatLabel.sizePolicy().hasHeightForWidth())
        self.timeSettingsFormatLabel.setSizePolicy(sizePolicy)

        self.horizontalLayout_7.addWidget(self.timeSettingsFormatLabel)

        self.timeSettingsFormatComboBox = QComboBox(self.timeSettingsWidget)
        self.timeSettingsFormatComboBox.addItem("")
        self.timeSettingsFormatComboBox.addItem("")
        self.timeSettingsFormatComboBox.addItem("")
        self.timeSettingsFormatComboBox.setObjectName(u"timeSettingsFormatComboBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.timeSettingsFormatComboBox.sizePolicy().hasHeightForWidth())
        self.timeSettingsFormatComboBox.setSizePolicy(sizePolicy2)

        self.horizontalLayout_7.addWidget(self.timeSettingsFormatComboBox)

        self.timeSettingsCustomFormatLabel = QLabel(self.timeSettingsWidget)
        self.timeSettingsCustomFormatLabel.setObjectName(u"timeSettingsCustomFormatLabel")

        self.horizontalLayout_7.addWidget(self.timeSettingsCustomFormatLabel)

        self.timeSettingsCustomFormatLineEdit = QLineEdit(self.timeSettingsWidget)
        self.timeSettingsCustomFormatLineEdit.setObjectName(u"timeSettingsCustomFormatLineEdit")

        self.horizontalLayout_7.addWidget(self.timeSettingsCustomFormatLineEdit)


        self.verticalLayout.addWidget(self.timeSettingsWidget)

        self.currentTimeWidget = QWidget(self.timeWidget)
        self.currentTimeWidget.setObjectName(u"currentTimeWidget")
        self.horizontalLayout_6 = QHBoxLayout(self.currentTimeWidget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.currentTimeButton = QPushButton(self.currentTimeWidget)
        self.currentTimeButton.setObjectName(u"currentTimeButton")
        sizePolicy1.setHeightForWidth(self.currentTimeButton.sizePolicy().hasHeightForWidth())
        self.currentTimeButton.setSizePolicy(sizePolicy1)

        self.horizontalLayout_6.addWidget(self.currentTimeButton)

        self.currentTimeStringLabel = QLabel(self.currentTimeWidget)
        self.currentTimeStringLabel.setObjectName(u"currentTimeStringLabel")
        sizePolicy.setHeightForWidth(self.currentTimeStringLabel.sizePolicy().hasHeightForWidth())
        self.currentTimeStringLabel.setSizePolicy(sizePolicy)

        self.horizontalLayout_6.addWidget(self.currentTimeStringLabel)

        self.currentTimeStringLineEdit = QLineEdit(self.currentTimeWidget)
        self.currentTimeStringLineEdit.setObjectName(u"currentTimeStringLineEdit")
        self.currentTimeStringLineEdit.setReadOnly(True)

        self.horizontalLayout_6.addWidget(self.currentTimeStringLineEdit)

        self.currentTimeStampLabel = QLabel(self.currentTimeWidget)
        self.currentTimeStampLabel.setObjectName(u"currentTimeStampLabel")

        self.horizontalLayout_6.addWidget(self.currentTimeStampLabel)

        self.currentTimeStampLineEdit = QLineEdit(self.currentTimeWidget)
        self.currentTimeStampLineEdit.setObjectName(u"currentTimeStampLineEdit")
        self.currentTimeStampLineEdit.setReadOnly(True)

        self.horizontalLayout_6.addWidget(self.currentTimeStampLineEdit)


        self.verticalLayout.addWidget(self.currentTimeWidget)

        self.timestampWidget = QWidget(self.timeWidget)
        self.timestampWidget.setObjectName(u"timestampWidget")
        self.horizontalLayout_3 = QHBoxLayout(self.timestampWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.timestampLabel = QLabel(self.timestampWidget)
        self.timestampLabel.setObjectName(u"timestampLabel")
        sizePolicy.setHeightForWidth(self.timestampLabel.sizePolicy().hasHeightForWidth())
        self.timestampLabel.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.timestampLabel)

        self.timestampLineEdit = QLineEdit(self.timestampWidget)
        self.timestampLineEdit.setObjectName(u"timestampLineEdit")

        self.horizontalLayout_3.addWidget(self.timestampLineEdit)

        self.timestampConvertButton = QPushButton(self.timestampWidget)
        self.timestampConvertButton.setObjectName(u"timestampConvertButton")

        self.horizontalLayout_3.addWidget(self.timestampConvertButton)

        self.timestampConvertResultLineEdit = QLineEdit(self.timestampWidget)
        self.timestampConvertResultLineEdit.setObjectName(u"timestampConvertResultLineEdit")
        self.timestampConvertResultLineEdit.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.timestampConvertResultLineEdit)


        self.verticalLayout.addWidget(self.timestampWidget)

        self.timestrWidget = QWidget(self.timeWidget)
        self.timestrWidget.setObjectName(u"timestrWidget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.timestrWidget.sizePolicy().hasHeightForWidth())
        self.timestrWidget.setSizePolicy(sizePolicy3)
        self.horizontalLayout = QHBoxLayout(self.timestrWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.timestrLabel = QLabel(self.timestrWidget)
        self.timestrLabel.setObjectName(u"timestrLabel")

        self.horizontalLayout.addWidget(self.timestrLabel)

        self.timestrLineEdit = QLineEdit(self.timestrWidget)
        self.timestrLineEdit.setObjectName(u"timestrLineEdit")

        self.horizontalLayout.addWidget(self.timestrLineEdit)

        self.timestrConvertButton = QPushButton(self.timestrWidget)
        self.timestrConvertButton.setObjectName(u"timestrConvertButton")

        self.horizontalLayout.addWidget(self.timestrConvertButton)

        self.timestrConvertResultLineEdit = QLineEdit(self.timestrWidget)
        self.timestrConvertResultLineEdit.setObjectName(u"timestrConvertResultLineEdit")
        self.timestrConvertResultLineEdit.setReadOnly(True)

        self.horizontalLayout.addWidget(self.timestrConvertResultLineEdit)


        self.verticalLayout.addWidget(self.timestrWidget)

        self.timeVerticalSpacer = QSpacerItem(20, 505, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.timeVerticalSpacer)

        self.tabWidget.addTab(self.timeWidget, "")
        self.jsonWidget = QWidget()
        self.jsonWidget.setObjectName(u"jsonWidget")
        self.verticalLayout_4 = QVBoxLayout(self.jsonWidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.jsonActionWidget = QWidget(self.jsonWidget)
        self.jsonActionWidget.setObjectName(u"jsonActionWidget")
        self.horizontalLayout_2 = QHBoxLayout(self.jsonActionWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.jsonFormatButton = QPushButton(self.jsonActionWidget)
        self.jsonFormatButton.setObjectName(u"jsonFormatButton")
        sizePolicy1.setHeightForWidth(self.jsonFormatButton.sizePolicy().hasHeightForWidth())
        self.jsonFormatButton.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.jsonFormatButton)

        self.jsonToYamlButton = QPushButton(self.jsonActionWidget)
        self.jsonToYamlButton.setObjectName(u"jsonToYamlButton")

        self.horizontalLayout_2.addWidget(self.jsonToYamlButton)

        self.jsonFromYamlButton = QPushButton(self.jsonActionWidget)
        self.jsonFromYamlButton.setObjectName(u"jsonFromYamlButton")

        self.horizontalLayout_2.addWidget(self.jsonFromYamlButton)

        self.jsonFormatIndentLabel = QLabel(self.jsonActionWidget)
        self.jsonFormatIndentLabel.setObjectName(u"jsonFormatIndentLabel")

        self.horizontalLayout_2.addWidget(self.jsonFormatIndentLabel)

        self.jsonFormatIndentComboBox = QComboBox(self.jsonActionWidget)
        self.jsonFormatIndentComboBox.addItem("")
        self.jsonFormatIndentComboBox.addItem("")
        self.jsonFormatIndentComboBox.addItem("")
        self.jsonFormatIndentComboBox.addItem("")
        self.jsonFormatIndentComboBox.setObjectName(u"jsonFormatIndentComboBox")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.jsonFormatIndentComboBox.sizePolicy().hasHeightForWidth())
        self.jsonFormatIndentComboBox.setSizePolicy(sizePolicy4)

        self.horizontalLayout_2.addWidget(self.jsonFormatIndentComboBox)

        self.jsonInputActionHorizontalSpacer = QSpacerItem(290, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.jsonInputActionHorizontalSpacer)

        self.jsonResultCopyButton = QPushButton(self.jsonActionWidget)
        self.jsonResultCopyButton.setObjectName(u"jsonResultCopyButton")

        self.horizontalLayout_2.addWidget(self.jsonResultCopyButton)


        self.verticalLayout_4.addWidget(self.jsonActionWidget)

        self.jsonEditWidget = QWidget(self.jsonWidget)
        self.jsonEditWidget.setObjectName(u"jsonEditWidget")
        self.horizontalLayout_4 = QHBoxLayout(self.jsonEditWidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.jsonTextEdit = QTextEdit(self.jsonEditWidget)
        self.jsonTextEdit.setObjectName(u"jsonTextEdit")
        font = QFont()
        font.setFamilies([u"Consolas"])
        font.setPointSize(13)
        self.jsonTextEdit.setFont(font)
        self.jsonTextEdit.setTabStopDistance(40.000000000000000)

        self.horizontalLayout_4.addWidget(self.jsonTextEdit)

        self.jsonResultTextEdit = QTextEdit(self.jsonEditWidget)
        self.jsonResultTextEdit.setObjectName(u"jsonResultTextEdit")
        self.jsonResultTextEdit.setFont(font)
        self.jsonResultTextEdit.setReadOnly(True)
        self.jsonResultTextEdit.setTabStopDistance(40.000000000000000)

        self.horizontalLayout_4.addWidget(self.jsonResultTextEdit)


        self.verticalLayout_4.addWidget(self.jsonEditWidget)

        self.tabWidget.addTab(self.jsonWidget, "")
        self.requestWidget = QWidget()
        self.requestWidget.setObjectName(u"requestWidget")
        self.verticalLayout_2 = QVBoxLayout(self.requestWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.requestTopWidget = QWidget(self.requestWidget)
        self.requestTopWidget.setObjectName(u"requestTopWidget")
        sizePolicy4.setHeightForWidth(self.requestTopWidget.sizePolicy().hasHeightForWidth())
        self.requestTopWidget.setSizePolicy(sizePolicy4)
        self.horizontalLayout_5 = QHBoxLayout(self.requestTopWidget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(12, 0, 12, 0)
        self.requestMethodComboBox = QComboBox(self.requestTopWidget)
        self.requestMethodComboBox.addItem("")
        self.requestMethodComboBox.addItem("")
        self.requestMethodComboBox.addItem("")
        self.requestMethodComboBox.addItem("")
        self.requestMethodComboBox.addItem("")
        self.requestMethodComboBox.setObjectName(u"requestMethodComboBox")
        sizePolicy1.setHeightForWidth(self.requestMethodComboBox.sizePolicy().hasHeightForWidth())
        self.requestMethodComboBox.setSizePolicy(sizePolicy1)

        self.horizontalLayout_5.addWidget(self.requestMethodComboBox)

        self.requestUrlLineEdit = QLineEdit(self.requestTopWidget)
        self.requestUrlLineEdit.setObjectName(u"requestUrlLineEdit")

        self.horizontalLayout_5.addWidget(self.requestUrlLineEdit)

        self.requestInvokeButton = QPushButton(self.requestTopWidget)
        self.requestInvokeButton.setObjectName(u"requestInvokeButton")

        self.horizontalLayout_5.addWidget(self.requestInvokeButton)


        self.verticalLayout_2.addWidget(self.requestTopWidget)

        self.requestMainWidget = QWidget(self.requestWidget)
        self.requestMainWidget.setObjectName(u"requestMainWidget")
        self.horizontalLayout_8 = QHBoxLayout(self.requestMainWidget)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.requestReqWidget = QWidget(self.requestMainWidget)
        self.requestReqWidget.setObjectName(u"requestReqWidget")
        self.verticalLayout_5 = QVBoxLayout(self.requestReqWidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 0, 0, 0)
        self.requestReqTopWidget = QWidget(self.requestReqWidget)
        self.requestReqTopWidget.setObjectName(u"requestReqTopWidget")
        self.horizontalLayout_9 = QHBoxLayout(self.requestReqTopWidget)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, 0, -1, 0)

        self.verticalLayout_5.addWidget(self.requestReqTopWidget)

        self.requestExportCurlButton = QPushButton(self.requestReqWidget)
        self.requestExportCurlButton.setObjectName(u"requestExportCurlButton")
        sizePolicy1.setHeightForWidth(self.requestExportCurlButton.sizePolicy().hasHeightForWidth())
        self.requestExportCurlButton.setSizePolicy(sizePolicy1)

        self.verticalLayout_5.addWidget(self.requestExportCurlButton)

        self.requestReqTabWidget = QTabWidget(self.requestReqWidget)
        self.requestReqTabWidget.setObjectName(u"requestReqTabWidget")
        self.requestHeadersWidget = QWidget()
        self.requestHeadersWidget.setObjectName(u"requestHeadersWidget")
        self.verticalLayout_8 = QVBoxLayout(self.requestHeadersWidget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.requestHeadersActionWidget = QWidget(self.requestHeadersWidget)
        self.requestHeadersActionWidget.setObjectName(u"requestHeadersActionWidget")
        self.horizontalLayout_11 = QHBoxLayout(self.requestHeadersActionWidget)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.requestHeadersAddButton = QPushButton(self.requestHeadersActionWidget)
        self.requestHeadersAddButton.setObjectName(u"requestHeadersAddButton")
        sizePolicy1.setHeightForWidth(self.requestHeadersAddButton.sizePolicy().hasHeightForWidth())
        self.requestHeadersAddButton.setSizePolicy(sizePolicy1)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ListAdd))
        self.requestHeadersAddButton.setIcon(icon)

        self.horizontalLayout_11.addWidget(self.requestHeadersAddButton)

        self.requestHeadersRemoveButton = QPushButton(self.requestHeadersActionWidget)
        self.requestHeadersRemoveButton.setObjectName(u"requestHeadersRemoveButton")
        sizePolicy1.setHeightForWidth(self.requestHeadersRemoveButton.sizePolicy().hasHeightForWidth())
        self.requestHeadersRemoveButton.setSizePolicy(sizePolicy1)
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ListRemove))
        self.requestHeadersRemoveButton.setIcon(icon1)

        self.horizontalLayout_11.addWidget(self.requestHeadersRemoveButton)

        self.requestHeadersResetButton = QPushButton(self.requestHeadersActionWidget)
        self.requestHeadersResetButton.setObjectName(u"requestHeadersResetButton")
        sizePolicy1.setHeightForWidth(self.requestHeadersResetButton.sizePolicy().hasHeightForWidth())
        self.requestHeadersResetButton.setSizePolicy(sizePolicy1)
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ViewRefresh))
        self.requestHeadersResetButton.setIcon(icon2)

        self.horizontalLayout_11.addWidget(self.requestHeadersResetButton)


        self.verticalLayout_8.addWidget(self.requestHeadersActionWidget)

        self.requestHeadersTableWidget = QTableWidget(self.requestHeadersWidget)
        if (self.requestHeadersTableWidget.columnCount() < 2):
            self.requestHeadersTableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.requestHeadersTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.requestHeadersTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.requestHeadersTableWidget.setObjectName(u"requestHeadersTableWidget")
        self.requestHeadersTableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.requestHeadersTableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.requestHeadersTableWidget.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.requestHeadersTableWidget.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.requestHeadersTableWidget.setColumnCount(2)
        self.requestHeadersTableWidget.horizontalHeader().setMinimumSectionSize(20)
        self.requestHeadersTableWidget.horizontalHeader().setDefaultSectionSize(120)
        self.requestHeadersTableWidget.horizontalHeader().setHighlightSections(False)
        self.requestHeadersTableWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.requestHeadersTableWidget.horizontalHeader().setStretchLastSection(True)
        self.requestHeadersTableWidget.verticalHeader().setVisible(True)
        self.requestHeadersTableWidget.verticalHeader().setMinimumSectionSize(20)

        self.verticalLayout_8.addWidget(self.requestHeadersTableWidget)

        self.requestReqTabWidget.addTab(self.requestHeadersWidget, "")
        self.requestReqBodyWidget = QWidget()
        self.requestReqBodyWidget.setObjectName(u"requestReqBodyWidget")
        self.verticalLayout_3 = QVBoxLayout(self.requestReqBodyWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.requestReqBodyTextEdit = QTextEdit(self.requestReqBodyWidget)
        self.requestReqBodyTextEdit.setObjectName(u"requestReqBodyTextEdit")
        self.requestReqBodyTextEdit.setFont(font)

        self.verticalLayout_3.addWidget(self.requestReqBodyTextEdit)

        self.requestReqTabWidget.addTab(self.requestReqBodyWidget, "")
        self.requestSettingsWidget = QWidget()
        self.requestSettingsWidget.setObjectName(u"requestSettingsWidget")
        sizePolicy3.setHeightForWidth(self.requestSettingsWidget.sizePolicy().hasHeightForWidth())
        self.requestSettingsWidget.setSizePolicy(sizePolicy3)
        self.formLayout = QFormLayout(self.requestSettingsWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy.ExpandingFieldsGrow)
        self.formLayout.setFormAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.requestSettingsConnectTimeoutLabel = QLabel(self.requestSettingsWidget)
        self.requestSettingsConnectTimeoutLabel.setObjectName(u"requestSettingsConnectTimeoutLabel")
        sizePolicy2.setHeightForWidth(self.requestSettingsConnectTimeoutLabel.sizePolicy().hasHeightForWidth())
        self.requestSettingsConnectTimeoutLabel.setSizePolicy(sizePolicy2)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.requestSettingsConnectTimeoutLabel)

        self.requestSettingsConnectTimeoutLineEdit = QLineEdit(self.requestSettingsWidget)
        self.requestSettingsConnectTimeoutLineEdit.setObjectName(u"requestSettingsConnectTimeoutLineEdit")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.requestSettingsConnectTimeoutLineEdit.sizePolicy().hasHeightForWidth())
        self.requestSettingsConnectTimeoutLineEdit.setSizePolicy(sizePolicy5)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.requestSettingsConnectTimeoutLineEdit)

        self.requestSettingsReadTimeoutLabel = QLabel(self.requestSettingsWidget)
        self.requestSettingsReadTimeoutLabel.setObjectName(u"requestSettingsReadTimeoutLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.requestSettingsReadTimeoutLabel)

        self.requestSettingsReadTimeoutLineEdit = QLineEdit(self.requestSettingsWidget)
        self.requestSettingsReadTimeoutLineEdit.setObjectName(u"requestSettingsReadTimeoutLineEdit")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.requestSettingsReadTimeoutLineEdit)

        self.requestReqTabWidget.addTab(self.requestSettingsWidget, "")

        self.verticalLayout_5.addWidget(self.requestReqTabWidget)


        self.horizontalLayout_8.addWidget(self.requestReqWidget)

        self.requestRespWidget = QWidget(self.requestMainWidget)
        self.requestRespWidget.setObjectName(u"requestRespWidget")
        self.verticalLayout_6 = QVBoxLayout(self.requestRespWidget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, 0, 0, 0)
        self.requestRespTopWidget = QWidget(self.requestRespWidget)
        self.requestRespTopWidget.setObjectName(u"requestRespTopWidget")
        self.horizontalLayout_10 = QHBoxLayout(self.requestRespTopWidget)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, 0, -1, 0)
        self.requestStatusLabel = QLabel(self.requestRespTopWidget)
        self.requestStatusLabel.setObjectName(u"requestStatusLabel")

        self.horizontalLayout_10.addWidget(self.requestStatusLabel)

        self.requestDurationLabel = QLabel(self.requestRespTopWidget)
        self.requestDurationLabel.setObjectName(u"requestDurationLabel")
        sizePolicy3.setHeightForWidth(self.requestDurationLabel.sizePolicy().hasHeightForWidth())
        self.requestDurationLabel.setSizePolicy(sizePolicy3)

        self.horizontalLayout_10.addWidget(self.requestDurationLabel)


        self.verticalLayout_6.addWidget(self.requestRespTopWidget)

        self.requestRespTabWidget = QTabWidget(self.requestRespWidget)
        self.requestRespTabWidget.setObjectName(u"requestRespTabWidget")
        self.requestRespBodyWidget = QWidget()
        self.requestRespBodyWidget.setObjectName(u"requestRespBodyWidget")
        self.verticalLayout_7 = QVBoxLayout(self.requestRespBodyWidget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.requestRespBodyTextEdit = QTextEdit(self.requestRespBodyWidget)
        self.requestRespBodyTextEdit.setObjectName(u"requestRespBodyTextEdit")
        self.requestRespBodyTextEdit.setFont(font)
        self.requestRespBodyTextEdit.setReadOnly(True)

        self.verticalLayout_7.addWidget(self.requestRespBodyTextEdit)

        self.requestRespTabWidget.addTab(self.requestRespBodyWidget, "")
        self.requestRespHeadersWidget = QWidget()
        self.requestRespHeadersWidget.setObjectName(u"requestRespHeadersWidget")
        self.verticalLayout_9 = QVBoxLayout(self.requestRespHeadersWidget)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.requestRespHeadersTableWidget = QTableWidget(self.requestRespHeadersWidget)
        if (self.requestRespHeadersTableWidget.columnCount() < 2):
            self.requestRespHeadersTableWidget.setColumnCount(2)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.requestRespHeadersTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.requestRespHeadersTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem3)
        self.requestRespHeadersTableWidget.setObjectName(u"requestRespHeadersTableWidget")
        self.requestRespHeadersTableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.requestRespHeadersTableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.requestRespHeadersTableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.requestRespHeadersTableWidget.setColumnCount(2)
        self.requestRespHeadersTableWidget.horizontalHeader().setMinimumSectionSize(20)
        self.requestRespHeadersTableWidget.horizontalHeader().setDefaultSectionSize(120)
        self.requestRespHeadersTableWidget.horizontalHeader().setHighlightSections(False)
        self.requestRespHeadersTableWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.requestRespHeadersTableWidget.horizontalHeader().setStretchLastSection(True)
        self.requestRespHeadersTableWidget.verticalHeader().setVisible(False)
        self.requestRespHeadersTableWidget.verticalHeader().setHighlightSections(False)

        self.verticalLayout_9.addWidget(self.requestRespHeadersTableWidget)

        self.requestRespTabWidget.addTab(self.requestRespHeadersWidget, "")
        self.requestRespDetailWidget = QWidget()
        self.requestRespDetailWidget.setObjectName(u"requestRespDetailWidget")
        self.verticalLayout_10 = QVBoxLayout(self.requestRespDetailWidget)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.requestRespDetailTextEdit = QTextEdit(self.requestRespDetailWidget)
        self.requestRespDetailTextEdit.setObjectName(u"requestRespDetailTextEdit")
        font1 = QFont()
        font1.setFamilies([u"Consolas"])
        self.requestRespDetailTextEdit.setFont(font1)
        self.requestRespDetailTextEdit.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.requestRespDetailTextEdit)

        self.requestRespTabWidget.addTab(self.requestRespDetailWidget, "")

        self.verticalLayout_6.addWidget(self.requestRespTabWidget)


        self.horizontalLayout_8.addWidget(self.requestRespWidget)


        self.verticalLayout_2.addWidget(self.requestMainWidget)

        self.tabWidget.addTab(self.requestWidget, "")

        self.gridLayout_4.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.retranslateUi(ToolWidget)

        self.tabWidget.setCurrentIndex(2)
        self.requestReqTabWidget.setCurrentIndex(0)
        self.requestRespTabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(ToolWidget)
    # setupUi

    def retranslateUi(self, ToolWidget):
        ToolWidget.setWindowTitle(QCoreApplication.translate("ToolWidget", u"ToolWidget", None))
        self.timeSettingsPrecisionLabel.setText(QCoreApplication.translate("ToolWidget", u"\u65f6\u95f4\u7cbe\u5ea6", None))
        self.timeSettingsPrecisionComboBox.setItemText(0, QCoreApplication.translate("ToolWidget", u"\u79d2", None))
        self.timeSettingsPrecisionComboBox.setItemText(1, QCoreApplication.translate("ToolWidget", u"\u6beb\u79d2", None))

        self.timeSettingsFormatLabel.setText(QCoreApplication.translate("ToolWidget", u"\u5b57\u7b26\u4e32\u683c\u5f0f", None))
        self.timeSettingsFormatComboBox.setItemText(0, QCoreApplication.translate("ToolWidget", u"\u9ed8\u8ba4\uff082006-01-02 15:04:05\uff09", None))
        self.timeSettingsFormatComboBox.setItemText(1, QCoreApplication.translate("ToolWidget", u"RFC3339\uff082006-01-02T15:04:05Z\uff09", None))
        self.timeSettingsFormatComboBox.setItemText(2, QCoreApplication.translate("ToolWidget", u"\u81ea\u5b9a\u4e49\u683c\u5f0f", None))

        self.timeSettingsCustomFormatLabel.setText(QCoreApplication.translate("ToolWidget", u"\u81ea\u5b9a\u4e49\u683c\u5f0f", None))
        self.currentTimeButton.setText(QCoreApplication.translate("ToolWidget", u"\u83b7\u53d6\u5f53\u524d\u65f6\u95f4", None))
        self.currentTimeStringLabel.setText(QCoreApplication.translate("ToolWidget", u"\u5b57\u7b26\u4e32", None))
        self.currentTimeStampLabel.setText(QCoreApplication.translate("ToolWidget", u"\u65f6\u95f4\u6233", None))
        self.timestampLabel.setText(QCoreApplication.translate("ToolWidget", u"\u65f6\u95f4\u6233 -> \u5b57\u7b26\u4e32", None))
        self.timestampConvertButton.setText(QCoreApplication.translate("ToolWidget", u"\u8f6c\u6362", None))
        self.timestrLabel.setText(QCoreApplication.translate("ToolWidget", u"\u5b57\u7b26\u4e32 -> \u65f6\u95f4\u6233", None))
        self.timestrConvertButton.setText(QCoreApplication.translate("ToolWidget", u"\u8f6c\u6362", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.timeWidget), QCoreApplication.translate("ToolWidget", u"\u65f6\u95f4\u5de5\u5177", None))
        self.jsonFormatButton.setText(QCoreApplication.translate("ToolWidget", u"\u683c\u5f0f\u5316JSON", None))
        self.jsonToYamlButton.setText(QCoreApplication.translate("ToolWidget", u"JSON\u8f6cYAML", None))
        self.jsonFromYamlButton.setText(QCoreApplication.translate("ToolWidget", u"YAML\u8f6cJSON", None))
        self.jsonFormatIndentLabel.setText(QCoreApplication.translate("ToolWidget", u"\u7f29\u8fdb", None))
        self.jsonFormatIndentComboBox.setItemText(0, QCoreApplication.translate("ToolWidget", u"\u65e0", None))
        self.jsonFormatIndentComboBox.setItemText(1, QCoreApplication.translate("ToolWidget", u"2", None))
        self.jsonFormatIndentComboBox.setItemText(2, QCoreApplication.translate("ToolWidget", u"4", None))
        self.jsonFormatIndentComboBox.setItemText(3, QCoreApplication.translate("ToolWidget", u"8", None))

        self.jsonResultCopyButton.setText(QCoreApplication.translate("ToolWidget", u"\u590d\u5236\u7ed3\u679c", None))
        self.jsonTextEdit.setPlaceholderText(QCoreApplication.translate("ToolWidget", u"\u8bf7\u8f93\u5165JSON\u6216YAML\u5b57\u7b26\u4e32", None))
        self.jsonResultTextEdit.setPlaceholderText(QCoreApplication.translate("ToolWidget", u"\u6b64\u5904\u5c55\u793a\u7ed3\u679c\uff0cReadOnly", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.jsonWidget), QCoreApplication.translate("ToolWidget", u"JSON\u5de5\u5177", None))
        self.requestMethodComboBox.setItemText(0, QCoreApplication.translate("ToolWidget", u"GET", None))
        self.requestMethodComboBox.setItemText(1, QCoreApplication.translate("ToolWidget", u"POST", None))
        self.requestMethodComboBox.setItemText(2, QCoreApplication.translate("ToolWidget", u"PUT", None))
        self.requestMethodComboBox.setItemText(3, QCoreApplication.translate("ToolWidget", u"DELETE", None))
        self.requestMethodComboBox.setItemText(4, QCoreApplication.translate("ToolWidget", u"PATCH", None))

        self.requestInvokeButton.setText(QCoreApplication.translate("ToolWidget", u"\u6267\u884c\u8bf7\u6c42", None))
        self.requestExportCurlButton.setText(QCoreApplication.translate("ToolWidget", u"\u5bfc\u51faCURL", None))
        self.requestHeadersAddButton.setText(QCoreApplication.translate("ToolWidget", u"\u65b0\u589e", None))
        self.requestHeadersRemoveButton.setText(QCoreApplication.translate("ToolWidget", u"\u5220\u9664", None))
        self.requestHeadersResetButton.setText(QCoreApplication.translate("ToolWidget", u"\u6062\u590d\u9ed8\u8ba4", None))
        ___qtablewidgetitem = self.requestHeadersTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("ToolWidget", u"Key", None));
        ___qtablewidgetitem1 = self.requestHeadersTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("ToolWidget", u"Value", None));
        self.requestReqTabWidget.setTabText(self.requestReqTabWidget.indexOf(self.requestHeadersWidget), QCoreApplication.translate("ToolWidget", u"Headers", None))
        self.requestReqBodyTextEdit.setPlaceholderText(QCoreApplication.translate("ToolWidget", u"\u8bf7\u5728\u6b64\u5904\u8f93\u5165Request-Body", None))
        self.requestReqTabWidget.setTabText(self.requestReqTabWidget.indexOf(self.requestReqBodyWidget), QCoreApplication.translate("ToolWidget", u"Body", None))
        self.requestSettingsConnectTimeoutLabel.setText(QCoreApplication.translate("ToolWidget", u"\u8fde\u63a5\u8d85\u65f6\uff08ms\uff09", None))
        self.requestSettingsReadTimeoutLabel.setText(QCoreApplication.translate("ToolWidget", u"\u8bfb\u53d6\u8d85\u65f6\uff08ms\uff09", None))
        self.requestReqTabWidget.setTabText(self.requestReqTabWidget.indexOf(self.requestSettingsWidget), QCoreApplication.translate("ToolWidget", u"Settings", None))
        self.requestStatusLabel.setText(QCoreApplication.translate("ToolWidget", u"\u72b6\u6001\uff1a", None))
        self.requestDurationLabel.setText(QCoreApplication.translate("ToolWidget", u"\u7528\u65f6\uff1a", None))
        self.requestRespBodyTextEdit.setPlaceholderText(QCoreApplication.translate("ToolWidget", u"\u6b64\u5904\u5c55\u793aResponse-Body", None))
        self.requestRespTabWidget.setTabText(self.requestRespTabWidget.indexOf(self.requestRespBodyWidget), QCoreApplication.translate("ToolWidget", u"Body", None))
        ___qtablewidgetitem2 = self.requestRespHeadersTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("ToolWidget", u"Key", None));
        ___qtablewidgetitem3 = self.requestRespHeadersTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("ToolWidget", u"Value", None));
        self.requestRespTabWidget.setTabText(self.requestRespTabWidget.indexOf(self.requestRespHeadersWidget), QCoreApplication.translate("ToolWidget", u"Headers", None))
        self.requestRespDetailTextEdit.setPlaceholderText(QCoreApplication.translate("ToolWidget", u"\u6b64\u5904\u5c55\u793a\u8bf7\u6c42\u6267\u884c\u8be6\u60c5", None))
        self.requestRespTabWidget.setTabText(self.requestRespTabWidget.indexOf(self.requestRespDetailWidget), QCoreApplication.translate("ToolWidget", u"\u6267\u884c\u8be6\u60c5", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.requestWidget), QCoreApplication.translate("ToolWidget", u"\u8bf7\u6c42\u5de5\u5177", None))
    # retranslateUi

