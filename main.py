import sys

from PyQt5 import QtWidgets
from main_win import Ui_MainWindow


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.configure()

    def configure(self):
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    win = MyWindow()
    win.show()

    app.exec_()