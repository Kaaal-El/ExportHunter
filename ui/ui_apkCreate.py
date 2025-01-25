# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'apkCreate.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFrame, QPushButton, QSizePolicy, QTextBrowser,
    QTextEdit, QWidget)

class Ui_apkCreate(object):
    def setupUi(self, apkCreate):
        if not apkCreate.objectName():
            apkCreate.setObjectName(u"apkCreate")
        apkCreate.resize(719, 620)
        self.buttonBox = QDialogButtonBox(apkCreate)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(610, 60, 81, 41))
        self.buttonBox.setOrientation(Qt.Orientation.Vertical)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Ok)
        self.apkCodeText = QTextEdit(apkCreate)
        self.apkCodeText.setObjectName(u"apkCodeText")
        self.apkCodeText.setGeometry(QRect(20, 20, 561, 461))
        self.line = QFrame(apkCreate)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(590, 110, 118, 3))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.outputText = QTextBrowser(apkCreate)
        self.outputText.setObjectName(u"outputText")
        self.outputText.setGeometry(QRect(20, 500, 561, 101))
        self.apkLaunch = QPushButton(apkCreate)
        self.apkLaunch.setObjectName(u"apkLaunch")
        self.apkLaunch.setGeometry(QRect(610, 20, 81, 32))
        self.refresh = QPushButton(apkCreate)
        self.refresh.setObjectName(u"refresh")
        self.refresh.setGeometry(QRect(610, 570, 91, 32))

        self.retranslateUi(apkCreate)
        self.buttonBox.accepted.connect(apkCreate.accept)
        self.buttonBox.rejected.connect(apkCreate.reject)

        QMetaObject.connectSlotsByName(apkCreate)
    # setupUi

    def retranslateUi(self, apkCreate):
        apkCreate.setWindowTitle(QCoreApplication.translate("apkCreate", u"Dialog", None))
        self.apkCodeText.setHtml(QCoreApplication.translate("apkCreate", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Arial';\"><br /></p></body></html>", None))
        self.apkLaunch.setText(QCoreApplication.translate("apkCreate", u"Launch", None))
        self.refresh.setText(QCoreApplication.translate("apkCreate", u"ReGenerate", None))
    # retranslateUi

