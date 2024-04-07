import sys

from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets

from main_win import Ui_MainWindow


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.configure()

        def configure(self):
            self.ok_btn.clicked.connect(self.change_label_after_clc)

        def change_label_clc(self):
            self.label.settext('1')



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    win = MyWindow()
    win.show()

    app.exec_()