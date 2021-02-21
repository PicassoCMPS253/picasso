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

    def pressed_okay(self):
        path = os.getcwd()
        file = QFileDialog.getOpenFileName(self, "Add a Folder", path, "(*.png, *.png, *.jpg, *.jpeg)")
        file.setFilter(QDir.Dirs)
        for f in os.scan(path):
            if f.path.endswith(".png") or f.path.endswith(".jpeg") or f.path.endswith(".jpg"):
                listofpics.append(f.path)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = AppWindow()
    w.show()
    sys.exit(app.exec_())
    

