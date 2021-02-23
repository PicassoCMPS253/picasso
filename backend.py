import os
from UI import *
from PyQt5.QtWidgets import QInputDialog, QLineEdit, QDialog, QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QIcon


listofpics = []
class AppWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self,parent=None):
        super(AppWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        self.ui.addButton.clicked.connect(self.pressed_okay)
        self.ui.gridLayoutWidget.setGeometry(QtCore.QRect(210, 90, 531, 361))
        self.ui.gridLayout.addWidget(self.ui.verticalScrollBar, 0, 3, 1, len(listofpics))
        self.loadImages()


    def pressed_okay(self):
        path = os.getcwd()
        file = QFileDialog.getOpenFileNames(self,"name",path,'Image Files(*.png *.jpg *.bmp *.xpm)')
        listofpics.append(file[0][0])
        self.ui.gridLayout.addWidget(self.ui.verticalScrollBar, 0, 3, len(listofpics), 1)
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


    def loadImages(self):
        '''
         My algorithm is:
         1- Create as many Pixmap instances as len(listofpics)
         2- Put them in the correct grid
         3- set the Pixmap instances to the listofpics elements
        '''
        
        # Create a list with the label names
        labelsNames = []
        for i in range(len(listofpics)):
            labelsNames.append("label_"+str(i))
        # Create the label instances
        for i in range(len(listofpics)):
            labelsNames[i] = QtWidgets.QLabel(self.ui.gridLayoutWidget)

            # Place the label in its correct place in the grid
            self.ui.gridLayout.addWidget(labelsNames[i], self.placeInGrid(i)[0], self.placeInGrid(i)[1],1,1)

            labelsNames[i].setObjectName(str(labelsNames[i]))
            labelsNames[i].setText("")
            labelsNames[i].setPixmap(QPixmap(listofpics[i]).scaled(150,120))


   





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = AppWindow()
    w.show()
    sys.exit(app.exec_())
    
