import sys

from PyQt5 import QtWidgets
from main_win import Ui_MainWindow


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.configure()

    def configure(self):
        self.btn_clear.clicked.connect(
            lambda: self.line_result.clear()
        )

        self.btn_eq.clicked.connect(self.__handle_equal)

        for btn, val in self.__map_btn_values():
            btn.clicked.connect(self.__handle(val))

    def __handle(self, val: str):
        def wrap():
            math_op = ["*", "-", "+", "/"]
            new_text = self.line_result.text()

            if new_text and (new_text[-1] in math_op) and (val in math_op):
                return

            new_text = self.line_result.text() + val

            new_text = new_text.replace("++", "+")
            new_text = new_text.replace("--", "-")
            new_text = new_text.replace("**", "*")
            new_text = new_text.replace("//", "/")

            self.line_result.setText(new_text)

        return wrap

    def __handle_equal(self):
        try:
            result = float(eval(self.line_result.text()))
        except:
            result = self.line_result.text()
            msg = QtWidgets.QMessageBox(self)
            msg.setText("Ошибка при вычислении")

            msg.exec_()

        self.line_result.setText(str(result))

    def __map_btn_values(self):
        return [
            (self.btn_0, "0"),
            (self.btn_1, "1"),
            (self.btn_2, "2"),
            (self.btn_3, "3"),
            (self.btn_4, "4"),
            (self.btn_5, "5"),
            (self.btn_6, "6"),
            (self.btn_7, "7"),
            (self.btn_8, "8"),
            (self.btn_9, "9"),

            (self.btn_add, "+"),
            (self.btn_diff, "-"),
            (self.btn_mul, "*"),
            (self.btn_div, "/"),
        ]

def create_msg_error(parent, msg_text/)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    win = MyWindow()
    win.show()

    app.exec_()
