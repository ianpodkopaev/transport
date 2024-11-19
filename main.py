import sys
from logic import estimate_approach_queue_resolution_time
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
letters = 'abcdefghijklmnopqrstuvwxyz'

# #const
# tQ = 0
# Kk = 0
# Ks=0
# Km=0
# ko = 0
# kl = 0
#
# q=[[],[]]
# c=0
# vehicletype=[[],[]]

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
        self.ui.tableWidget_3.setColumnCount(7)
        self.ui.tableWidget_3.setHorizontalHeaderLabels(["№ полосы", "выход","начало","конец","R","Delay","Ky"])
        self.ui.tableWidget_4.setRowCount(0)
        self.ui.tableWidget_4.setColumnCount(3)
        self.ui.tableWidget_4.setHorizontalHeaderLabels(['Л', 'Г' ,'О'])
        self.ui.tableWidget_5.setRowCount(0)
        self.ui.tableWidget_5.setColumnCount(6)
        self.ui.tableWidget_5.setHorizontalHeaderLabels(['№ полосы', 'выход' ,'Л', 'Г', 'О', 'Кпов'])
        self.ui.tableWidget_6.setRowCount(0)
        self.ui.tableWidget_6.setColumnCount(2)
        self.ui.tableWidget_6.setHorizontalHeaderLabels(['№ полосы', 'загрузка'])

        self.ui.lineEdit_2.textEdited.connect(self.TableOne)
        self.ui.lineEdit.textEdited.connect(self.TableOne)

        self.ui.lineEdit_2.textEdited.connect(self.TableTwo)
        self.ui.lineEdit_4.textEdited.connect(self.TableTwo)

        self.ui.lineEdit_2.textEdited.connect(self.TableThree)
        self.ui.lineEdit_4.textEdited.connect(self.TableThree)

        self.ui.lineEdit_2.textEdited.connect(self.TableFour)
        self.ui.lineEdit_4.textEdited.connect(self.TableFour)

        self.ui.lineEdit_2.textEdited.connect(self.TableSix)
        self.ui.lineEdit_4.textEdited.connect(self.TableSix)

        self.ui.lineEdit_2.textEdited.connect(self.FinalTable)
        self.ui.lineEdit_4.textEdited.connect(self.FinalTable) 
        self.ui.pushButton.clicked.connect(self.FinalTable)

        self.ui.pushButton.clicked.connect(self.ButtonClick)
        self.TableFour()

    def TableOne(self, text):
        try:

            rowsCount = int(self.ui.lineEdit_2.text())+1
            self.ui.tableWidget.setRowCount(rowsCount)

            input_letter = self.ui.lineEdit.text().strip()

            alphabet = letters[:rowsCount]

            for row in range(rowsCount):
                self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(input_letter))
                letter = alphabet[row % len(alphabet)]
                self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(letter))

        except ValueError:
            return
    def TableTwo(self, text):
        try:
            linesCount = int(self.ui.lineEdit_4.text())
            outputsCount = int(self.ui.lineEdit_2.text())+1

        except ValueError:
            return  

        totalRows = linesCount * outputsCount
        self.ui.tableWidget_2.setRowCount(totalRows)


        alphabet = letters[:outputsCount]

        for i in range(totalRows):
            groupNumber = (i // outputsCount) + 1
            self.ui.tableWidget_2.setItem(i, 0, QTableWidgetItem(str(groupNumber)))
            letter = alphabet[i % len(alphabet)]
            self.ui.tableWidget_2.setItem(i, 1, QTableWidgetItem(letter))

            for col in range(2, self.ui.tableWidget_2.columnCount()):
                combo = QComboBox()
                combo.addItems(["True", "False"])
                self.ui.tableWidget_2.setCellWidget(i, col, combo)
    def TableThree(self,text):
        try:
            linesCount = int(self.ui.lineEdit_4.text())
            outputsCount = int(self.ui.lineEdit_2.text())+1
        except ValueError:
            return  

        totalRows = linesCount * outputsCount
        self.ui.tableWidget_3.setRowCount(totalRows)

        alphabet = letters[:outputsCount]

        for i in range(totalRows):
            groupNumber = (i // outputsCount) + 1
            self.ui.tableWidget_3.setItem(i, 0, QTableWidgetItem(str(groupNumber)))
            letter = alphabet[i % len(alphabet)]
            self.ui.tableWidget_3.setItem(i, 1, QTableWidgetItem(letter))
    def TableFour(self):
      #  try:
         #   linesCount = int(self.ui.lineEdit_4.text())
       #     outputsCount = int(self.ui.lineEdit_2.text()) + 1
     #   except ValueError:
      #      return

       # totalRows = linesCount * outputsCount
        self.ui.tableWidget_4.setRowCount(1)

       # alphabet = letters[:outputsCount]

        #for i in range(totalRows):
         #   groupNumber = (i // outputsCount) + 1
          #  self.ui.tableWidget_4.setItem(i, 0, QTableWidgetItem(str(groupNumber)))
           # letter = alphabet[i % len(alphabet)]
            #self.ui.tableWidget_4.setItem(i, 1, QTableWidgetItem(letter))

        # for column in range(self.ui.tableWidget_4.columnCount()):
        #     item = QTableWidgetItem()
        #     item.setFlags(item.flags() | Qt.ItemIsEditable)
        #     self.ui.tableWidget_4.setItem(0, column, item)
            # try:
        #     linesCount = int(self.ui.lineEdit_4.text())
        #     outputsCount = int(self.ui.lineEdit_2.text()) + 1
        # except ValueError:
        #     return
        #
        # totalRows = linesCount * outputsCount
        # self.ui.tableWidget_4.setRowCount(totalRows)
        #
        # for row in range(rowsCount):
        #     self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(input_letter))
        #     letter = alphabet[row % len(alphabet)]
        #     self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(letter))
        #
        # for column in range(self.ui.tableWidget_4.columnCount()):
        #     item = QTableWidgetItem()
        #     item.setFlags(item.flags() | Qt.ItemIsEditable)
        #     self.ui.tableWidget_4.setItem(0, column, item)
    def TableSix(self, text):
        try:
            linesCount = int(self.ui.lineEdit_4.text())

        except ValueError:
            return


        self.ui.tableWidget_6.setRowCount(linesCount)


        for i in range(linesCount):
            groupNumber = (i+1)
            self.ui.tableWidget_6.setItem(i, 0, QTableWidgetItem(str(groupNumber)))
    def FinalTable(self):
        try:
            linesCount = int(self.ui.lineEdit_4.text())
            outputsCount = int(self.ui.lineEdit_2.text())+1
        except ValueError:
            return  

        totalRows = linesCount * outputsCount
        self.ui.tableWidget_5.setRowCount(totalRows)

        alphabet = letters[:outputsCount]

        for i in range(totalRows):
            groupNumber = (i // outputsCount) + 1
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

    def ButtonClick(self):
        try:
            cycleLength = int(self.ui.lineEdit_3.text())
            nActualOutCount = int(self.ui.lineEdit_2.text())
            InLanesCount = int(self.ui.lineEdit_4.text())
            LaneQueue=[]
            reductionByDynamicCoeffs=[]
        # for coeffs
            for col in range(0, 3):  # Колонки 2, 3, 4
                coeff_item = self.ui.tableWidget_4.item(0, col)
                if coeff_item is not None:
                    try:
                        coeff = float(coeff_item.text())
                        reductionByDynamicCoeffs.append(coeff)
                    except ValueError:
                        reductionByDynamicCoeffs.append(0)
                else:
                    reductionByDynamicCoeffs.append(0)

            print(reductionByDynamicCoeffs)
        except ValueError:
            return
           #для lanequeue - переделать
          #  for row in range(self.ui.tableWidget_4.rowCount()):
           #     lane_number = int(self.ui.tableWidget_4.item(row, 0).text())
            #    L_item = self.ui.tableWidget_4.item(row, 0)
             #   G_item = self.ui.tableWidget_4.item(row, 1)
              #  O_item = self.ui.tableWidget_4.item(row, 2)

              #  L = int(L_item.text()) if L_item is not None else 0
              #  G = int(G_item.text()) if G_item is not None else 0
              #  O = int(O_item.text()) if O_item is not None else 0

              #  total = L + G + O
              #  LaneQueue.append([lane_number, total])






app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
