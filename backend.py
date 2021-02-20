import os
from UI import *
from PyQt5.QtWidgets import QInputDialog, QLineEdit, QDialog, QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QIcon



class AppWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self,parent=None):
        super(AppWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        self.ui.addButton.clicked.connect(self.pressed_okay)

    def pressed_okay(self):
        path = os.getcwd()
        file = QFileDialog.getOpenFileName(self, "Open Image", path, "Images (*.png, *.png, *.jpeg)")
        print(file[0])

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = AppWindow()
    w.show()
    sys.exit(app.exec_())
    

