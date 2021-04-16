import os
from sample import *
from PyQt5.QtWidgets import QInputDialog, QLineEdit, QDialog, QFileDialog, QScrollArea
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QIcon
import face_recognition
import numpy as np
from faceDetection import *


listofpics = [] #make as a dictionary and import to JSON
albums["All Photos"] = listofpics


class AppWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self,parent=None):
        super(AppWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        self.ui.addImage.clicked.connect(self.pressed_picture)
        self.ui.addFolder.clicked.connect(self.pressed_folder)
        self.ui.gridLayoutWidget.setGeometry(QtCore.QRect(210, 90, 531, 361))
        self.loadImages()
        self.ui.comboBox.currentTextChanged.connect(self.comboChanged)



    #Combo Album Functions
    def add(self, name="Untitled"):
        self.ui.comboBox.addItem(name) #implement automatic naming from facedetection.py
    

    def remove(self):
        self.ui.comboBox.removeItem(self.ui.comboBox.currentIndex())
    
    def comboChanged(self):
        selectedAlbum = self.ui.comboBox.currentText()
        self.loadImages(selectedAlbum)
 

    def rename(self):
        text = self.ui.albumName.text()
        if(text == ""):
            self.ui.comboBox.setItemText(self.ui.comboBox.currentIndex(),"Untitled")
        else:
            self.ui.comboBox.setItemText(self.ui.comboBox.currentIndex(),text)
        self.ui.albumName.clear()

    def clearLayout(self, layout):
            if layout is not None:
                while layout.count():
                    item = layout.takeAt(0)
                    widget = item.widget()
                    if widget is not None:
                        widget.deleteLater()
                    else:
                        self.clearLayout(item.layout())



    def pressed_picture(self):
        path = os.getcwd()
        file = QFileDialog.getOpenFileNames(self,"name",path, "Images (*.jpg *.png *.jpeg)")
        self.scale()
        
        print("1:", file[0])
        listofpics.extend(file[0])
        print(listofpics)

        faceExists(listofpics) 

        comboItems = [self.ui.comboBox.itemText(i) for i in range(self.ui.comboBox.count())]
        
        for element in sorted(albums):
            if element not in comboItems:
                  self.add(element)

        self.loadImages()


    def pressed_folder(self):
        path = "/Users/ehab/Desktop/cmps278/HW1/HW1/img/"
        lst = os.listdir(path) #lst has now the image pathnames
        count=1
        self.scale()
        for i in range(0,len(lst)):
            if (lst[i][-3::]=='jpg' and count!=3):
                lst.append(lst[i])
                count+=1
        for j in range(1,len(lst)):
            listofpics.append(path + str(lst[j]))
            albums["All Photos"] = listofpics
        self.ui.gridLayout.addWidget(self.ui.verticalScrollBar, 0, 3, len(listofpics),1)
        self.loadImages()



    

    def scale(self):
        size = (len(listofpics)//6)+1 
        self.ui.gridLayoutWidget.setGeometry(QtCore.QRect(210, 90, 531, 361*size))
    





    def placeInGrid(self, n):

        '''
        The member function .addWidget() takes a tuple of 5 parm's (a0: QWidget, row: int, column: int, rowSpan: int, columnSpan: int) 

        placeInGrid will generate a tuple of the 4 numbers to place the n'th item when the screen is loaded

        The formula is:

        n/numberOfColumns = Quotient R Remainder 

        n = the element number
        numberOfColumns: is the number of columns in the grid
        Quotient = will give us the row place
        Remainder = will give us the column place

        NOTE! COUNTING STARTS FROM 0 FOR ALL
        '''

        numberOfColumns = 3
        row = n//numberOfColumns
        col = n%numberOfColumns
        return(row,col,1,1) 




    def loadImages(self, album="All Photos"):

        self.clearLayout(self.ui.gridLayout)

        '''
         My algorithm is:
         1- Create as many Pixmap instances as len(listofpics)
         2- Put them in the correct grid
         3- set the Pixmap instances to the listofpics elements
        '''
        
        # Create a list with the label names
        labelsNames = []
        for i in range(len(albums[album])):
            labelsNames.append("label_"+str(i))

        # Create the label instances
        for i in range(len(albums[album])):
            labelsNames[i] = QtWidgets.QLabel(self.ui.gridLayoutWidget)

            # Place the label in its correct place in the grid
            self.ui.gridLayout.addWidget(labelsNames[i], self.placeInGrid(i)[0], self.placeInGrid(i)[1], 1, 1)
            labelsNames[i].setObjectName(str(labelsNames[i]))
            labelsNames[i].setText("")
            labelsNames[i].setPixmap(QPixmap(list(albums[album])[i]).scaled(200,210,100))
            labelsNames[i].setScaledContents(True)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = AppWindow()
    w.show()
    sys.exit(app.exec_())
    

