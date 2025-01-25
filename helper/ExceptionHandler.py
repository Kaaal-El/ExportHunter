# This Python file uses the following encoding: utf-8

from PySide6.QtWidgets import QMessageBox

class ExceptionHandler:
    def __init__():
        pass

    def warning(title,info):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Critical)
        # msg_box.setWindowTitle("Error")
        msg_box.setText(title)
        msg_box.setInformativeText(info)
        msg_box.exec()
