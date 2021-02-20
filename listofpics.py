from ui import *
from PyQt5.QtWidgets import QInputDialog, QLineEdit, QDialog
from PyQt5 import QtCore, QtGui, QtWidgets




class AppWindow(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        self.ui.addButton.clicked.connect(self.pressed_okay)

    def pressed_okay(self):
        print("c")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = AppWindow()
    w.show()
    sys.exit(app.exec_())
    

