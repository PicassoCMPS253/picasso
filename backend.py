import os
from sample import *
from PyQt5.QtWidgets import QInputDialog, QLineEdit, QDialog, QFileDialog, QScrollArea
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QIcon
import face_recognition
import numpy as np
from faceDetection import *
import json

try:
    listofpics = albums["All Photos"]
except:
    listofpics = []

try:
    albums["All Photos"] = albums["All Photos"]
except:
    albums["All Photos"] = listofpics


try:
    with open(str(currentWorkingDirectory)+'/albumsNamingDB.json', 'r') as json_file:
        names = json.load(json_file)
except ValueError:
    names = {"All Photos":"All Photos"}



width = 481
print(listofpics)



class AppWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self,parent=None):
        super(AppWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        self.ui.addImage.clicked.connect(self.addPicture)
        self.ui.rename.clicked.connect(self.rename)
        self.ui.gridLayoutWidget.setGeometry(QtCore.QRect(210, 90, 531, 361))
        self.loadImages()
        self.loadAlbums()
        self.loadNames()
        self.ui.comboBox.currentTextChanged.connect(self.comboChanged)



    #Combo Album Functions 
    def add(self, name="Untitled"):
        self.ui.comboBox.addItem(name) 
    
    
    def comboChanged(self):
        selectedAlbum = self.ui.comboBox.currentText()
        self.loadImages(names[selectedAlbum])
 

    def rename(self):
        text = self.ui.input.text()


        currentIndex = self.ui.comboBox.currentIndex()
        
        if(text != "" and currentIndex!=0):

            currentName = self.ui.comboBox.currentText()
            names[text] = currentName
            self.ui.comboBox.setItemText(currentIndex, text)
            del names[currentName]
            with open(str(currentWorkingDirectory)+'/albumsNamingDB.json', 'w') as json_file:
                json.dump(names, json_file)


        self.ui.input.clear()

    def clearLayout(self, layout):

            if layout is not None:
                while layout.count():
                    item = layout.takeAt(0)
                    widget = item.widget()
                    if widget is not None:
                        widget.deleteLater()
                    else:
                        self.clearLayout(item.layout())



    def addPicture(self):
        path = os.getcwd()
        file = QFileDialog.getOpenFileNames(self,"name",path, "Images (*.jpg *.png *.jpeg)")
        
        listofpics.extend(file[0]) # Merge list of pics with the added files
        print(listofpics)

        faceExists(listofpics) # Update the albums dict with faces in albums
        self.loadAlbums()
        self.ui.comboBox.setCurrentIndex(0) # When adding a picture(s) send the user back to the all photos album
        
        self.loadImages()
    
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
            labelsNames[i].setPixmap(QPixmap(list(albums[album])[i]).scaled(250,250))
            labelsNames[i].setScaledContents(False)

    def loadAlbums(self):
        comboItems = [self.ui.comboBox.itemText(i) for i in range(self.ui.comboBox.count())] # List of albums in the comboBox
        index = 1
        for element in sorted(albums): # add albums to the comboBox
            print(element)
            if element not in comboItems and ((self.findKeyByValue(names,element)) == None):
                    self.add(element)
                    if (self.findKeyByValue(names,element)) == None:
                        names[element]=element


    def loadNames(self):
        comboItems = [self.ui.comboBox.itemText(i) for i in range(self.ui.comboBox.count())] # List of albums in the comboBox

        for i in comboItems:
            if i in names.values():
                itemIndex = 0
                for itemIndex in range(len(comboItems)):
                    if i == self.ui.comboBox.itemText(itemIndex):
                        self.ui.comboBox.setItemText(itemIndex, self.findKeyByValue(names,i))
                        print("hit, ", self.findKeyByValue(names,i), i, names)
                    else:
                        print("miss", itemIndex)

    def findKeyByValue(self, dict, valueE):
        for key, value in dict.items():
            if valueE == value:
                return key



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = AppWindow()
    w.show()
    sys.exit(app.exec_())
    

