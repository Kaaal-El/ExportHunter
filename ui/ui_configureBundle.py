# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'configureBundle.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QAbstractScrollArea, QApplication, QDialog,
    QDialogButtonBox, QHeaderView, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_configureBundle(object):
    def setupUi(self, configureBundle):
        if not configureBundle.objectName():
            configureBundle.setObjectName(u"configureBundle")
        configureBundle.resize(624, 261)
        self.buttonBox = QDialogButtonBox(configureBundle)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(510, 20, 81, 241))
        self.buttonBox.setOrientation(Qt.Orientation.Vertical)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.bundleTable = QTableWidget(configureBundle)
        if (self.bundleTable.columnCount() < 3):
            self.bundleTable.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.bundleTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.bundleTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.bundleTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.bundleTable.setObjectName(u"bundleTable")
        self.bundleTable.setGeometry(QRect(30, 19, 441, 171))
        self.bundleTable.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.bundleTable.setGridStyle(Qt.PenStyle.SolidLine)
        self.bundleTable.horizontalHeader().setStretchLastSection(True)
        self.addBundle = QPushButton(configureBundle)
        self.addBundle.setObjectName(u"addBundle")
        self.addBundle.setGeometry(QRect(40, 210, 100, 32))
        self.removeBundle = QPushButton(configureBundle)
        self.removeBundle.setObjectName(u"removeBundle")
        self.removeBundle.setGeometry(QRect(160, 210, 100, 32))

        self.retranslateUi(configureBundle)
        self.buttonBox.accepted.connect(configureBundle.accept)
        self.buttonBox.rejected.connect(configureBundle.reject)

        QMetaObject.connectSlotsByName(configureBundle)
    # setupUi

    def retranslateUi(self, configureBundle):
        configureBundle.setWindowTitle(QCoreApplication.translate("configureBundle", u"Dialog", None))
        ___qtablewidgetitem = self.bundleTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("configureBundle", u"Type", None));
        ___qtablewidgetitem1 = self.bundleTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("configureBundle", u"Key", None));
        ___qtablewidgetitem2 = self.bundleTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("configureBundle", u"Value", None));
        self.addBundle.setText(QCoreApplication.translate("configureBundle", u"Add", None))
        self.removeBundle.setText(QCoreApplication.translate("configureBundle", u"Remove", None))
    # retranslateUi

