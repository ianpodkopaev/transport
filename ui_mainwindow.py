# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSplitter, QTableWidget,
    QTableWidgetItem, QWidget)
# import icons_rc

class Ui_w_main(object):
    def setupUi(self, w_main):
        if not w_main.objectName():
            w_main.setObjectName(u"w_main")
        w_main.resize(1296, 791)
        font = QFont()
        font.setPointSize(12)
        w_main.setFont(font)
        self.pushButton = QPushButton(w_main)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(830, 590, 361, 171))
        self.tableWidget_5 = QTableWidget(w_main)
        self.tableWidget_5.setObjectName(u"tableWidget_5")
        self.tableWidget_5.setGeometry(QRect(30, 440, 661, 321))
        self.splitter_5 = QSplitter(w_main)
        self.splitter_5.setObjectName(u"splitter_5")
        self.splitter_5.setGeometry(QRect(20, 70, 600, 48))
        self.splitter_5.setOrientation(Qt.Orientation.Horizontal)
        self.splitter = QSplitter(self.splitter_5)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Vertical)
        self.label = QLabel(self.splitter)
        self.label.setObjectName(u"label")
        self.splitter.addWidget(self.label)
        self.lineEdit = QLineEdit(self.splitter)
        self.lineEdit.setObjectName(u"lineEdit")
        self.splitter.addWidget(self.lineEdit)
        self.splitter_5.addWidget(self.splitter)
        self.splitter_2 = QSplitter(self.splitter_5)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Orientation.Vertical)
        self.label_2 = QLabel(self.splitter_2)
        self.label_2.setObjectName(u"label_2")
        self.splitter_2.addWidget(self.label_2)
        self.lineEdit_2 = QLineEdit(self.splitter_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.splitter_2.addWidget(self.lineEdit_2)
        self.splitter_5.addWidget(self.splitter_2)
        self.splitter_3 = QSplitter(self.splitter_5)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setOrientation(Qt.Orientation.Vertical)
        self.label_3 = QLabel(self.splitter_3)
        self.label_3.setObjectName(u"label_3")
        self.splitter_3.addWidget(self.label_3)
        self.lineEdit_3 = QLineEdit(self.splitter_3)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.splitter_3.addWidget(self.lineEdit_3)
        self.splitter_5.addWidget(self.splitter_3)
        self.splitter_4 = QSplitter(self.splitter_5)
        self.splitter_4.setObjectName(u"splitter_4")
        self.splitter_4.setOrientation(Qt.Orientation.Vertical)
        self.label_4 = QLabel(self.splitter_4)
        self.label_4.setObjectName(u"label_4")
        self.splitter_4.addWidget(self.label_4)
        self.lineEdit_4 = QLineEdit(self.splitter_4)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.splitter_4.addWidget(self.lineEdit_4)
        self.splitter_5.addWidget(self.splitter_4)
        self.splitter_11 = QSplitter(w_main)
        self.splitter_11.setObjectName(u"splitter_11")
        self.splitter_11.setGeometry(QRect(20, 170, 1280, 213))
        self.splitter_11.setOrientation(Qt.Orientation.Horizontal)
        self.splitter_6 = QSplitter(self.splitter_11)
        self.splitter_6.setObjectName(u"splitter_6")
        self.splitter_6.setOrientation(Qt.Orientation.Vertical)
        self.label_5 = QLabel(self.splitter_6)
        self.label_5.setObjectName(u"label_5")
        self.splitter_6.addWidget(self.label_5)
        self.tableWidget = QTableWidget(self.splitter_6)
        self.tableWidget.setObjectName(u"tableWidget")
        self.splitter_6.addWidget(self.tableWidget)
        self.splitter_11.addWidget(self.splitter_6)
        self.splitter_7 = QSplitter(self.splitter_11)
        self.splitter_7.setObjectName(u"splitter_7")
        self.splitter_7.setOrientation(Qt.Orientation.Vertical)
        self.label_6 = QLabel(self.splitter_7)
        self.label_6.setObjectName(u"label_6")
        self.splitter_7.addWidget(self.label_6)
        self.tableWidget_2 = QTableWidget(self.splitter_7)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.splitter_7.addWidget(self.tableWidget_2)
        self.splitter_11.addWidget(self.splitter_7)
        self.splitter_8 = QSplitter(self.splitter_11)
        self.splitter_8.setObjectName(u"splitter_8")
        self.splitter_8.setOrientation(Qt.Orientation.Vertical)
        self.label_7 = QLabel(self.splitter_8)
        self.label_7.setObjectName(u"label_7")
        self.splitter_8.addWidget(self.label_7)
        self.tableWidget_3 = QTableWidget(self.splitter_8)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.splitter_8.addWidget(self.tableWidget_3)
        self.splitter_11.addWidget(self.splitter_8)
        self.splitter_9 = QSplitter(self.splitter_11)
        self.splitter_9.setObjectName(u"splitter_9")
        self.splitter_9.setOrientation(Qt.Orientation.Vertical)
        self.label_8 = QLabel(self.splitter_9)
        self.label_8.setObjectName(u"label_8")
        self.splitter_9.addWidget(self.label_8)
        self.tableWidget_4 = QTableWidget(self.splitter_9)
        self.tableWidget_4.setObjectName(u"tableWidget_4")
        self.splitter_9.addWidget(self.tableWidget_4)
        self.splitter_11.addWidget(self.splitter_9)
        self.splitter_10 = QSplitter(self.splitter_11)
        self.splitter_10.setObjectName(u"splitter_10")
        self.splitter_10.setOrientation(Qt.Orientation.Vertical)
        self.splitter_11.addWidget(self.splitter_10)

        self.retranslateUi(w_main)

        QMetaObject.connectSlotsByName(w_main)
    # setupUi

    def retranslateUi(self, w_main):
        w_main.setWindowTitle(QCoreApplication.translate("w_main", u"Transport", None))
        self.pushButton.setText(QCoreApplication.translate("w_main", u"Count", None))
        self.label.setText(QCoreApplication.translate("w_main", u"Entrence", None))
        self.label_2.setText(QCoreApplication.translate("w_main", u"Outputs", None))
        self.label_3.setText(QCoreApplication.translate("w_main", u"Cycle duration", None))
        self.label_4.setText(QCoreApplication.translate("w_main", u"Lanes", None))
        self.label_5.setText(QCoreApplication.translate("w_main", u"Intecity", None))
        self.label_6.setText(QCoreApplication.translate("w_main", u"TrafficSceme", None))
        self.label_7.setText(QCoreApplication.translate("w_main", u"Intervals", None))
        self.label_8.setText(QCoreApplication.translate("w_main", u"Radius", None))
    # retranslateUi

