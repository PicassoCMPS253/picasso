# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sampleui.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        def setupUi(self, MainWindow):
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1440, 767)
        #Main Window
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        #Add Folder Button
        self.addFolder = QtWidgets.QPushButton(self.centralwidget)
        self.addFolder.setGeometry(QtCore.QRect(470, 40, 113, 32))
        self.addFolder.setObjectName("addFolder")
        #Add Image Button
        self.addImage = QtWidgets.QPushButton(self.centralwidget)
        self.addImage.setGeometry(QtCore.QRect(630, 40, 113, 32))
        self.addImage.setObjectName("addImage")
        #Drop Down 
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(20, 160, 161, 26))
        self.comboBox.setObjectName("comboBox")
        #Album
        self.Album = QtWidgets.QLabel(self.centralwidget)
        self.Album.setGeometry(QtCore.QRect(90, 80, 61, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Album.setFont(font)
        self.Album.setObjectName("Album")
        self.input = QtWidgets.QLineEdit(self.centralwidget)
        self.input.setGeometry(QtCore.QRect(20, 110, 151, 21))
        self.input.setObjectName("input")
        #Rename Button
        self.rename = QtWidgets.QPushButton(self.centralwidget)
        self.rename.setGeometry(QtCore.QRect(190, 110, 71, 31))
        self.rename.setObjectName("rename")
        #MenuBar 
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1440, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        #Status Bar
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        #Scroll Area
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(340, 110, 481, 481))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaContents = QtWidgets.QWidget()
        self.scrollAreaContents.setGeometry(QtCore.QRect(0, 0, 481, 481))
        self.scrollAreaContents.setObjectName("scrollAreaContents")
        #Grid
        self.gridLayoutWidget = QtWidgets.QWidget(self.scrollAreaContents)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(-1, 0, 481, 481))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        #Scroll Bar
        self.verticalScrollBar = QtWidgets.QScrollBar(self.scrollAreaContents)
        self.verticalScrollBar.setGeometry(QtCore.QRect(400, 0, 20, 381))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.scrollArea.setWidget(self.gridLayoutWidget)
        MainWindow.setCentralWidget(self.centralwidget)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
       


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.addFolder.setText(_translate("MainWindow", "Add Folder"))
        self.addImage.setText(_translate("MainWindow", "Add Photo"))
        self.Album.setText(_translate("MainWindow", "Album"))
        self.rename.setText(_translate("MainWindow", "Rename"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
