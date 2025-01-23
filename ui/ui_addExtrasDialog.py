# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addExtrasDialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialog,
    QDialogButtonBox, QFrame, QLabel, QLineEdit,
    QSizePolicy, QWidget)

class Ui_addExtrasDialog(object):
    def setupUi(self, addExtrasDialog):
        if not addExtrasDialog.objectName():
            addExtrasDialog.setObjectName(u"addExtrasDialog")
        addExtrasDialog.resize(437, 223)
        self.buttonBox = QDialogButtonBox(addExtrasDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(60, 180, 341, 32))
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.label = QLabel(addExtrasDialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 101, 31))
        self.label.setAutoFillBackground(True)
        self.label.setFrameShape(QFrame.Shape.NoFrame)
        self.label_2 = QLabel(addExtrasDialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 56, 71, 31))
        self.label_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.label_3 = QLabel(addExtrasDialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 100, 71, 31))
        self.label_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.label_4 = QLabel(addExtrasDialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 139, 71, 31))
        self.label_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.line = QFrame(addExtrasDialog)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(17, 30, 391, 20))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.typeInput = QLineEdit(addExtrasDialog)
        self.typeInput.setObjectName(u"typeInput")
        self.typeInput.setGeometry(QRect(110, 60, 301, 31))
        self.keyInput = QLineEdit(addExtrasDialog)
        self.keyInput.setObjectName(u"keyInput")
        self.keyInput.setGeometry(QRect(110, 100, 301, 31))
        self.valueInput = QLineEdit(addExtrasDialog)
        self.valueInput.setObjectName(u"valueInput")
        self.valueInput.setGeometry(QRect(110, 140, 301, 31))
        self.bundleCheckBox = QCheckBox(addExtrasDialog)
        self.bundleCheckBox.setObjectName(u"bundleCheckBox")
        self.bundleCheckBox.setGeometry(QRect(20, 179, 101, 31))

        self.retranslateUi(addExtrasDialog)
        self.buttonBox.accepted.connect(addExtrasDialog.accept)
        self.buttonBox.rejected.connect(addExtrasDialog.reject)

        QMetaObject.connectSlotsByName(addExtrasDialog)
    # setupUi

    def retranslateUi(self, addExtrasDialog):
        addExtrasDialog.setWindowTitle(QCoreApplication.translate("addExtrasDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("addExtrasDialog", u"Add Extras :", None))
        self.label_2.setText(QCoreApplication.translate("addExtrasDialog", u"Type :", None))
        self.label_3.setText(QCoreApplication.translate("addExtrasDialog", u"Key :", None))
        self.label_4.setText(QCoreApplication.translate("addExtrasDialog", u"Value :", None))
#if QT_CONFIG(tooltip)
        self.typeInput.setToolTip(QCoreApplication.translate("addExtrasDialog", u"<html><head/><body><p>E.g. --es, --ez</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.bundleCheckBox.setText(QCoreApplication.translate("addExtrasDialog", u"Bundlle", None))
    # retranslateUi

