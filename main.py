import sys

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHeaderView, QLabel,
    QLineEdit, QPushButton, QScrollArea, QSizePolicy,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QComboBox)

from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from ui_mainwindow import Ui_w_main

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_w_main()
        self.ui.setupUi(self)

        self.ui.tableWidget.setRowCount(0)
        self.ui.tableWidget.setColumnCount(5)
        self.ui.tableWidget.setHorizontalHeaderLabels(["вход", "выход","Л","Г","О"])
        self.ui.tableWidget_2.setRowCount(0)
        self.ui.tableWidget_2.setColumnCount(5)
        self.ui.tableWidget_2.setHorizontalHeaderLabels(["№ полосы", "выход","Л","Г","О"])
        self.ui.tableWidget_3.setRowCount(0)
        self.ui.tableWidget_3.setColumnCount(5)
        self.ui.tableWidget_3.setHorizontalHeaderLabels(["№ полосы", "выход","R","Delay","Ky"])
        self.ui.tableWidget_4.setRowCount(0)
        self.ui.tableWidget_4.setColumnCount(3)
        self.ui.tableWidget_4.setHorizontalHeaderLabels(['Л', 'Г' ,'О'])
        self.ui.tableWidget_5.setRowCount(0)
        self.ui.tableWidget_5.setColumnCount(6)
        self.ui.tableWidget_5.setHorizontalHeaderLabels(['№ полосы', 'выход' ,'Л', 'Г', 'О', 'Кпов'])

        self.ui.lineEdit_2.textEdited.connect(self.TableOne)
        self.ui.lineEdit.textEdited.connect(self.TableOne)

        self.ui.lineEdit_2.textEdited.connect(self.TableTwo)
        self.ui.lineEdit_4.textEdited.connect(self.TableTwo)

        self.ui.lineEdit_2.textEdited.connect(self.TableThree)
        self.ui.lineEdit_4.textEdited.connect(self.TableThree) 

        self.ui.lineEdit_2.textEdited.connect(self.FinalTable)
        self.ui.lineEdit_4.textEdited.connect(self.FinalTable) 
        self.ui.pushButton.clicked.connect(self.FinalTable)

        self.TableFour()


    def TableOne(self, text):
        try:
            rowsCount = int(self.ui.lineEdit_2.text())
            self.ui.tableWidget_2.setRowCount(rowsCount)

            input_letter = self.ui.lineEdit.text().strip()

            alphabet = 'abcdefghijklmnopqrstuvwxyz'

            for row in range(rowsCount):
                self.ui.tableWidget_2.setItem(row, 0, QTableWidgetItem(input_letter))
                letter = alphabet[row % len(alphabet)]
                self.ui.tableWidget_2.setItem(row, 1, QTableWidgetItem(letter))

        except ValueError:
            return
            


    def TableTwo(self, text):
        try:
            groupCount = int(self.ui.lineEdit_4.text())
            repeatCount = int(self.ui.lineEdit_2.text())
        except ValueError:
            return  

        totalRows = groupCount * repeatCount
        self.ui.tableWidget_3.setRowCount(totalRows)

        alphabet = ['a', 'b', 'c']

        for i in range(totalRows):
            groupNumber = (i // repeatCount) + 1
            self.ui.tableWidget_3.setItem(i, 0, QTableWidgetItem(str(groupNumber)))
            letter = alphabet[i % len(alphabet)]
            self.ui.tableWidget_3.setItem(i, 1, QTableWidgetItem(letter))

            for col in range(2, self.ui.tableWidget_3.columnCount()):
                combo = QComboBox()
                combo.addItems(["True", "False"])
                self.ui.tableWidget_3.setCellWidget(i, col, combo)


    def TableThree(self,text):
        try:
            groupCount = int(self.ui.lineEdit_4.text())
            repeatCount = int(self.ui.lineEdit_2.text())
        except ValueError:
            return  

        totalRows = groupCount * repeatCount
        self.ui.tableWidget_4.setRowCount(totalRows)

        alphabet = ['a', 'b', 'c']

        for i in range(totalRows):
            groupNumber = (i // repeatCount) + 1
            self.ui.tableWidget_4.setItem(i, 0, QTableWidgetItem(str(groupNumber)))
            letter = alphabet[i % len(alphabet)]
            self.ui.tableWidget_4.setItem(i, 1, QTableWidgetItem(letter)) 


    def TableFour(self):
        self.ui.tableWidget_5.setRowCount(1)
        
        for column in range(self.ui.tableWidget_5.columnCount()):
            item = QTableWidgetItem()
            item.setFlags(item.flags() | Qt.ItemIsEditable)
            self.ui.tableWidget_5.setItem(0, column, item)


    def FinalTable(self):
        try:
            groupCount = int(self.ui.lineEdit_4.text())
            repeatCount = int(self.ui.lineEdit_2.text())
        except ValueError:
            return  

        totalRows = groupCount * repeatCount
        self.ui.tableWidget_5.setRowCount(totalRows)

        alphabet = ['a', 'b', 'c']

        for i in range(totalRows):
            groupNumber = (i // repeatCount) + 1
            self.ui.tableWidget_5.setItem(i, 0, QTableWidgetItem(str(groupNumber)))
            letter = alphabet[i % len(alphabet)]
            self.ui.tableWidget_5.setItem(i, 1, QTableWidgetItem(letter)) 


        for row in range(self.ui.tableWidget_4.rowCount()):
            r_item = self.ui.tableWidget_4.item(row, 2)
            if r_item is not None:
                try:
                    R = float(r_item.text())
                    Kпов = 1 + (1.525 / R)
                    self.ui.tableWidget_5.setItem(row, 5, QTableWidgetItem("%.4f" % Kпов))
                except ValueError:
                    return


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
