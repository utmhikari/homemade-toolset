import sys
from typing import Optional

from PySide6 import QtCore, QtWidgets, QtGui

from .view.main_window import MainWindow


APP: Optional[QtWidgets.QApplication] = None


def run():
    global APP
    APP = QtWidgets.QApplication([])

    window = MainWindow()
    window.ensure_center()
    window.show()

    sys.exit(APP.exec())
