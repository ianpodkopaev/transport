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
import numpy as np

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
        self.ui.pushButton.clicked.connect(self.FinalTable)

        self.ui.lineEdit_2.textEdited.connect(self.TableTwo)
        self.ui.lineEdit_4.textEdited.connect(self.TableTwo)
        self.ui.pushButton.clicked.connect(self.TableTwo)

        self.ui.lineEdit_2.textEdited.connect(self.TableThree)
        self.ui.lineEdit_4.textEdited.connect(self.TableThree)
        self.ui.pushButton.clicked.connect(self.TableThree)

        self.ui.lineEdit_2.textEdited.connect(self.TableFour)
        self.ui.lineEdit_4.textEdited.connect(self.TableFour)
        self.ui.pushButton.clicked.connect(self.TableFour)

        self.ui.lineEdit_2.textEdited.connect(self.TableSix)
        self.ui.lineEdit_4.textEdited.connect(self.TableSix)
        self.ui.pushButton.clicked.connect(self.TableSix)

        self.ui.lineEdit_2.textEdited.connect(self.FinalTable)
        self.ui.lineEdit_4.textEdited.connect(self.FinalTable) 
        self.ui.pushButton.clicked.connect(self.FinalTable)

        self.ui.pushButton.clicked.connect(self.ButtonClick4)
        self.ui.pushButton.clicked.connect(self.ButtonClick2)
        self.ui.pushButton.clicked.connect(self.ButtonClick1)
        self.ui.pushButton.clicked.connect(self.ButtonClick3)
        self.ui.pushButton.clicked.connect(self.lanequeue)

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
            outputsCount = int(self.ui.lineEdit_2.text()) + 1
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
                # Получаем текущий виджет в ячейке, если он есть
                combo = self.ui.tableWidget_2.cellWidget(i, col)

                # Если виджета нет, создаем новый
                if combo is None:
                    combo = QComboBox()
                    combo.addItems(["True", "False"])
                    self.ui.tableWidget_2.setCellWidget(i, col, combo)



    # def TableTwo(self, text):
    #     try:
    #         linesCount = int(self.ui.lineEdit_4.text())
    #         outputsCount = int(self.ui.lineEdit_2.text())+1
    #
    #     except ValueError:
    #         return
    #
    #     totalRows = linesCount * outputsCount
    #     self.ui.tableWidget_2.setRowCount(totalRows)
    #
    #
    #     alphabet = letters[:outputsCount]
    #
    #     for i in range(totalRows):
    #         groupNumber = (i // outputsCount) + 1
    #         self.ui.tableWidget_2.setItem(i, 0, QTableWidgetItem(str(groupNumber)))
    #         letter = alphabet[i % len(alphabet)]
    #         self.ui.tableWidget_2.setItem(i, 1, QTableWidgetItem(letter))
    #
    #         for col in range(2, self.ui.tableWidget_2.columnCount()):
    #             combo = QComboBox()
    #             combo.addItems(["True", "False"])
    #             self.ui.tableWidget_2.setCellWidget(i, col, combo)
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




    def ButtonClick4(self):
        try:

            reductionByDynamicCoeffs = []
        # for coeffs
            # лго коэффициенты
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
            print("reductionByDynamicCoeffs")
            print(reductionByDynamicCoeffs)
            print("------")
            return(reductionByDynamicCoeffs)
        except ValueError:
            return

    def ButtonClick2(self):
        try:
            outputsCount = int(self.ui.lineEdit_2.text()) + 1
            linesCount = int(self.ui.lineEdit_4.text())
            veh_types = 3

            # Инициализация массива значениями False
            traffic_array = np.full((linesCount, outputsCount, veh_types), False)


            # Сопоставление индексов направлений (Л, Г, О) с измерением veh_types
            for i in range(linesCount):  # Перебираем линии
                for j in range(outputsCount):  # Перебираем выходы
                    for k in range(veh_types):  # Перебираем типы (Л, Г, О)
                        # Читаем значение из QComboBox
                        combo = self.ui.tableWidget_2.cellWidget(j, k+2)  # Столбцы с 2 (Л, Г, О)

                        if combo:  # Если виджет существует
                            selected_value = combo.currentText().strip().lower()  # Получаем текст
                            # Преобразуем в True/False
                            traffic_array[i][j][k] = selected_value == "true"

            print("Filled traffic_array:")
            print(traffic_array)
            return(traffic_array)
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

    def ButtonClick1(self):
        try:
            outputsCount = int(self.ui.lineEdit_2.text()) + 1
            veh_types = 3
            veh_types_array = np.full((outputsCount, veh_types), 0)
            for veh in range(veh_types):
                for out in range(outputsCount):
                    item = self.ui.tableWidget.item(out,veh+2)  # Столбцы начинаются с 2
                    if item is not None:
                        # Преобразуем значение в тип int или bool в зависимости от необходимости
                            veh_types_array[out][veh] = int(item.text().strip())  # Если это числовое значение

            print("INtencity")
            print(veh_types_array)
            return veh_types_array
        except ValueError:
            return()

    def ButtonClick3(self):
        try:
            outputsCount = int(self.ui.lineEdit_2.text()) + 1
            linesCount = int(self.ui.lineEdit_4.text())
            rows =5
            lines = outputsCount*linesCount
            intervals_array = np.full((lines, rows), 0)


            for i in range(lines):  # Перебираем линии
                for j in range(rows):
                    item = self.ui.tableWidget_3.item(i,j + 2)  # Столбцы начинаются с 2
                    if item is not None:
                        # Преобразуем значение в тип int или bool в зависимости от необходимости
                        intervals_array[i][j] = int(item.text())  # Если это числовое значение
            print("Intervals")
            print(intervals_array)
            return (intervals_array)
        except ValueError:
            return

    def deltaq(self):
        linesCount = int(self.ui.lineEdit_4.text())
        cycleTime = int(self.ui.lineEdit_3.text())
        outputsCount = int(self.ui.lineEdit_2.text()) + 1
        deltaQ = np.full((outputsCount), 0)

        veh_types_array = np.sum(self.ButtonClick1(), axis=1)
        print(1111)
        print(veh_types_array)
        print("Lanequeue")
        print(deltaQ)
        for out in range (outputsCount):
                    deltaQ[out]=cycleTime * veh_types_array[out]
        print(deltaQ)
        return(deltaQ)

    def lanequeue(self):
        linesCount = int(self.ui.lineEdit_4.text())
        cycleTime = int(self.ui.LineEdit_3.text())
        outputsCount = int(self.ui.lineEdit_2.text()) + 1
        deltaQ=self.deltaq()
        for line in range(linesCount):
            for out in range (outputsCount):
                for veh in range (3):
                    print()
#deltaQ[o,k]=q[o,k]*c

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

