from PyQt5 import QtCore, QtGui, uic, QtWidgets
import sys
from math import sqrt


# 메인 윈도우 창
class MainWindow(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = uic.loadUi("GUI.ui", self)
        self.ui.show()

        self.formula = []
        self.formula_show = []
        self.result = 0

    def textUpdate(self):
        formula_show = ""
        for i in self.formula_show:
            for j in i:
                formula_show += j

        self.mainText.setText(formula_show)

    def btn0(self):
        self.formula.append("0")
        self.formula_show.append("0")
        self.textUpdate()

    def btn1(self):
        self.formula.append("1")
        self.formula_show.append("1")
        self.textUpdate()

    def btn2(self):
        self.formula.append("2")
        self.formula_show.append("2")
        self.textUpdate()

    def btn3(self):
        self.formula.append("3")
        self.formula_show.append("3")
        self.textUpdate()

    def btn4(self):
        self.formula.append("4")
        self.formula_show.append("4")
        self.textUpdate()

    def btn5(self):
        self.formula.append("5")
        self.formula_show.append("5")
        self.textUpdate()

    def btn6(self):
        self.formula.append("6")
        self.formula_show.append("6")
        self.textUpdate()

    def btn7(self):
        self.formula.append("7")
        self.formula_show.append("7")
        self.textUpdate()

    def btn8(self):
        self.formula.append("8")
        self.formula_show.append("8")
        self.textUpdate()

    def btn9(self):
        self.formula.append("9")
        self.formula_show.append("9")
        self.textUpdate()

    def btndot(self):
        self.formula.append(".")
        self.formula_show.append(".")
        self.textUpdate()

    def btnbrace(self):
        self.textUpdate()

    def btnpls(self):
        self.formula.append("+")
        self.formula_show.append(" + ")
        self.textUpdate()

    def btnmin(self):
        self.formula.append("-")
        self.formula_show.append(" - ")
        self.textUpdate()

    def btnmul(self):
        self.formula.append("*")
        self.formula_show.append(" × ")
        self.textUpdate()

    def btndiv(self):
        self.formula.append("/")
        self.formula_show.append(" ÷ ")
        self.textUpdate()

    def btnsqr(self):
        self.formula.append("**")
        self.formula_show.append(" ^ ")
        self.textUpdate()

    def btnroot(self):
        self.formula.append(" sqrt(")
        self.formula_show.append(" √")
        self.textUpdate()

    def btnper(self):
        self.textUpdate()

    def btnclr(self):
        self.formula.clear()
        self.formula_show.clear()
        self.textUpdate()

    def btnback(self):
        self.formula.pop()
        self.formula_show.pop()
        self.textUpdate()

    def btnequal(self):
        formula = ""
        for i in self.formula:
            for j in i:
                formula += j

        try:
            self.result = str(eval(formula))
            self.formula.clear()
            self.formula_show.clear()
            self.formula.append(self.result)
            self.formula_show.append(self.result)
            self.mainText.setText(self.result)
            self.koreanText.setText("")
        except:
            self.koreanText.setText("올바른 수식을 입력해 주세요")


# 앱 실행
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Window = MainWindow(None)
    p = Window.palette()
    p.setColor(Window.backgroundRole(), QtGui.QColor(200, 200, 200))
    Window.setPalette(p)
    Window.show()
    app.exec_()
