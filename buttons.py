import sys
import os
from PyQt5.QtWidgets import (QApplication, QWidget,QFileDialog, QTextEdit, QPushButton, QLabel, QVBoxLayout)
from PyQt5.QtGui import QPixmap


class UI_MainWindow(QWidget):
    def __init__(self):
        super(UI_MainWindow, self).__init__()
        self.resize(1000,800)
        self.b1 = QPushButton("Add")
        self.b1.clicked.connect(self.openfolder)
        self.label = QLabel()

        layout = QVBoxLayout()
        layout.addWidget(self.label)  
        layout.addWidget(self.b1)
        self.setLayout(layout)

    def openfolder(self):
        while True: 
            path = os.getcwd()
            file = QFileDialog.getOpenFileName(self, "Open an image", path)#this line opens the directory of the current path. 
            self.label.setPixmap(QPixmap(file)) #this line just opens the photo
            print(file[0]) 
            #instead of print(file) i want a list array that 
            #is stored on a separate .py file, which updates every time i append
            #to it from this main file. 
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwin = UI_MainWindow()
    mainwin.show()
    sys.exit(app.exec_())