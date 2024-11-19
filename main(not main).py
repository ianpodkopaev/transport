import sys
import math

from PySide6.QtWidgets import (QApplication,QTableWidgetItem, QComboBox)
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from Algorithm import Ui_Form

letters = 'abcdefghijklmnopqrstuvwxyz'

#const
StandardSaturation = 3
Tloss = 10
IG = 7
Cycle = 60
n = 0
reductionByConditionCoeffs = [1, 1]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.tableWidget_2.setRowCount(0)
        self.ui.tableWidget_2.setColumnCount(5)
        self.ui.tableWidget_2.setHorizontalHeaderLabels(["вход", "выход","Л","Г","О"])
        self.ui.tableWidget_3.setRowCount(0)
        self.ui.tableWidget_3.setColumnCount(5)
        self.ui.tableWidget_3.setHorizontalHeaderLabels(["№ полосы", "выход","Л","Г","О"])
        self.ui.tableWidget_4.setRowCount(0)
        self.ui.tableWidget_4.setColumnCount(7)
        self.ui.tableWidget_4.setHorizontalHeaderLabels(["№ полосы", "выход",'нач зел','кон зел',"R","Delay","Ky"])
        self.ui.tableWidget_5.setRowCount(0)
        self.ui.tableWidget_5.setColumnCount(5)
        self.ui.tableWidget_5.setHorizontalHeaderLabels(['№ полосы','выход','Л', 'Г' ,'О'])
        self.ui.tableWidget_6.setRowCount(0)
        self.ui.tableWidget_6.setColumnCount(6)
        self.ui.tableWidget_6.setHorizontalHeaderLabels(['№ полосы', 'выход' ,'Л', 'Г', 'О', 'Кпов'])
        self.ui.tableWidget_7.setColumnCount(2)
        self.ui.tableWidget_7.setHorizontalHeaderLabels(['№ полосы', 'загрузка'])

        self.ui.lineEdit_2.textEdited.connect(self.TableOne)
        self.ui.lineEdit.textEdited.connect(self.TableOne)

        self.ui.lineEdit_2.textEdited.connect(self.TableTwo)
        self.ui.lineEdit_4.textEdited.connect(self.TableTwo)

        self.ui.lineEdit_2.textEdited.connect(self.TableThree)
        self.ui.lineEdit_4.textEdited.connect(self.TableThree) 

        self.ui.lineEdit_2.textEdited.connect(self.TableFour)
        self.ui.lineEdit_4.textEdited.connect(self.TableFour) 

        self.ui.lineEdit_2.textEdited.connect(self.FinalTable)
        self.ui.lineEdit_4.textEdited.connect(self.FinalTable) 
        self.ui.pushButton_2.clicked.connect(self.FinalTable)
        
        self.ui.lineEdit_4.textEdited.connect(self.FinalTable2) 

        self.ui.lineEdit_2.textEdited.connect(self.algorithm)
        self.ui.lineEdit_4.textEdited.connect(self.algorithm)
        self.ui.lineEdit_5.textEdited.connect(self.algorithm)
        self.ui.pushButton_2.clicked.connect(self.algorithm)


        self.TableFour()


    def TableOne(self, text):
        try:
            rowsCount = int(self.ui.lineEdit_2.text()) + 1
            self.ui.tableWidget_2.setRowCount(rowsCount)

            input_letter = self.ui.lineEdit.text().strip()

            alphabet = letters[:rowsCount]

            for row in range(rowsCount):
                self.ui.tableWidget_2.setItem(row, 0, QTableWidgetItem(input_letter))
                letter = alphabet[row % len(alphabet)]
                self.ui.tableWidget_2.setItem(row, 1, QTableWidgetItem(letter))

        except ValueError:
            return
            


    def TableTwo(self, text):
        try:
            groupCount = int(self.ui.lineEdit_4.text())
            repeatCount = int(self.ui.lineEdit_2.text()) + 1
        except ValueError:
            return  

        totalRows = groupCount * repeatCount
        self.ui.tableWidget_3.setRowCount(totalRows)

        alphabet = letters[:repeatCount]

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
            repeatCount = int(self.ui.lineEdit_2.text()) + 1
        except ValueError:
            return  

        totalRows = groupCount * repeatCount
        self.ui.tableWidget_4.setRowCount(totalRows)

        alphabet = letters[:repeatCount]

        for i in range(totalRows):
            groupNumber = (i // repeatCount) + 1
            self.ui.tableWidget_4.setItem(i, 0, QTableWidgetItem(str(groupNumber)))
            letter = alphabet[i % len(alphabet)]
            self.ui.tableWidget_4.setItem(i, 1, QTableWidgetItem(letter)) 


    def TableFour(self):
        try:
            groupCount = int(self.ui.lineEdit_4.text())
            repeatCount = int(self.ui.lineEdit_2.text()) + 1
        except ValueError:
            return  

        totalRows = groupCount * repeatCount
        self.ui.tableWidget_5.setRowCount(totalRows)

        alphabet = letters[:repeatCount]

        for i in range(totalRows):
            groupNumber = (i // repeatCount) + 1
            self.ui.tableWidget_5.setItem(i, 0, QTableWidgetItem(str(groupNumber)))
            letter = alphabet[i % len(alphabet)]
            self.ui.tableWidget_5.setItem(i, 1, QTableWidgetItem(letter))
        #for column in range(self.ui.tableWidget_5.columnCount()):
        #    item = QTableWidgetItem()
        #    item.setFlags(item.flags() | Qt.ItemIsEditable)
        #    self.ui.tableWidget_5.setItem(0, column, item)


    def FinalTable(self):
        try:
            groupCount = int(self.ui.lineEdit_4.text())
            repeatCount = int(self.ui.lineEdit_2.text()) + 1
        except ValueError:
            return  

        totalRows = groupCount * repeatCount
        self.ui.tableWidget_6.setRowCount(totalRows)

        alphabet = letters[:repeatCount]

        for i in range(totalRows):
            groupNumber = (i // repeatCount) + 1
            self.ui.tableWidget_6.setItem(i, 0, QTableWidgetItem(str(groupNumber)))
            letter = alphabet[i % len(alphabet)]
            self.ui.tableWidget_6.setItem(i, 1, QTableWidgetItem(letter)) 


        for row in range(self.ui.tableWidget_4.rowCount()):
            r_item = self.ui.tableWidget_4.item(row, 4)
            if r_item is not None:
                try:
                    R = float(r_item.text())
                    Kпов = 1 + (1.525 / R)
                    self.ui.tableWidget_6.setItem(row, 5, QTableWidgetItem("%.4f" % Kпов))
                except ValueError:
                    return


    def algorithm(self):
        try:
            InLanes = int(self.ui.lineEdit_4.text())
            OutCount = int(self.ui.lineEdit_2.text())
        except:
            return
        
        AccumulatedVolume = 0
        rowContribution = 0
        LaneQueue = []
        reductionByDynamicCoeffs = []

        for col in range(2, 5):  # Колонки 2, 3, 4
            coeff_item = self.ui.tableWidget_5.item(0, col)
            if coeff_item is not None:
                try:
                    coeff = float(coeff_item.text())
                    reductionByDynamicCoeffs.append(coeff)
                except ValueError:
                    reductionByDynamicCoeffs.append(0)
            else:
                reductionByDynamicCoeffs.append(0)

        for row in range(self.ui.tableWidget_5.rowCount()):
            lane_number = int(self.ui.tableWidget_5.item(row, 0).text())
            L_item = self.ui.tableWidget_5.item(row, 2)
            G_item = self.ui.tableWidget_5.item(row, 3)
            O_item = self.ui.tableWidget_5.item(row, 4)
            
            L = int(L_item.text()) if L_item is not None else 0
            G = int(G_item.text()) if G_item is not None else 0
            O = int(O_item.text()) if O_item is not None else 0
            
            total = L + G + O
            LaneQueue.append([lane_number, total])
            

        for row1 in range(self.ui.tableWidget_4.rowCount()):
            r_item = self.ui.tableWidget_4.item(row1, 4)
            R = float(r_item.text())
        for i in range(InLanes):
            for j in range(OutCount):
                km = 1.0 + (1.525 / R)

                for k in range(len(reductionByDynamicCoeffs)):
                    rowContribution += LaneQueue[i][1] * reductionByDynamicCoeffs[k] * km

                if i < len(reductionByConditionCoeffs):
                    rowContribution *= reductionByConditionCoeffs[i]

                AccumulatedVolume += rowContribution

        x = AccumulatedVolume / (StandardSaturation * (IG  - Tloss))
        fullCycles = max(0, math.ceil(x))  # Полные циклы не могут быть отрицательными
        lTQ = (AccumulatedVolume / StandardSaturation) + Tloss +  (fullCycles * Cycle)

        self.ui.lineEdit_5.setText(f"{lTQ:.2f}")

        print(lTQ)


    def FinalTable2(self):
        try:
            totalRows = int(self.ui.lineEdit_4.text())
        except ValueError:
            return  

        self.ui.tableWidget_7.setRowCount(totalRows)

        for i in range(totalRows):
            groupNumber = i + 1
            self.ui.tableWidget_7.setItem(i, 0, QTableWidgetItem(str(groupNumber)))       
    




    def EstimateApprachQueueResolution(self, AccumulatedVolume):
        # Q = 0
        # for iOut in range(0, out + 1):
        #     for Itype in range(0, Type + 1):
        #         Q += N[out][Type] * K[Type] * K[iOut] * Kl


        Xl = AccumulatedVolume / (StandardSaturation * (IG - Tloss) )
        lTQ = (AccumulatedVolume / StandardSaturation) + Tloss +  (Xl * Cycle)

        return lTQ

        # for row in range(self.ui.tableWinget_2.rowCount()):
        #     laneQueue = self.ui.tableWidget_2.item(row, 2)
        #     if laneQueue is not None:
        #         try:

        #         except:
        #             return
           



app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()