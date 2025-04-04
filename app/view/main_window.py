from PySide6 import QtWidgets
from PySide6.QtWidgets import QMainWindow, QMessageBox
from .ui.main_window import Ui_MainWindow
from .tool_widget import ToolWidget
from PySide6.QtGui import QScreen


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self._init_actions()
        self._init_widget()

    def _init_actions(self):
        self.ui.actionAbout.triggered.connect(self.show_about)
        self.ui.actionExit.triggered.connect(self.close)

        self.ui.actionSupport.triggered.connect(self.show_support)

    def _init_widget(self):
        self.setCentralWidget(ToolWidget())

    def closeEvent(self, event):
        reply = QMessageBox.question(
            self, '确认', '是否要退出程序？',
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.Yes)
        if reply == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()

    def ensure_center(self):
        """https://www.loekvandenouweland.com/content/pyside6-center-window.html"""
        center = QScreen.availableGeometry(QtWidgets.QApplication.primaryScreen()).center()
        geo = self.frameGeometry()
        geo.moveCenter(center)
        self.move(geo.topLeft())

    def show_about(self):
        title = self.ui.actionAbout.text()
        QMessageBox.information(self, title, '由HiKari亲手打造')

    def show_support(self):
        title = self.ui.actionSupport.text()
        QMessageBox.information(self, title, '请联系HiKari以获取官方支持')
