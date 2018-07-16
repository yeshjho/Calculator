from PyQt5 import QtCore, QtGui, uic, QtWidgets
import sys
from math import sqrt

CIPHER = ['', '만', '억', '조', '경', '해', '자', '양', '구', '간', '정', '재', '극']


# 메인 윈도우 창
class MainWindow(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = uic.loadUi("GUI.ui", self)
        self.ui.show()

        self.formula = []
        self.formula_show = []
        self.result = 0

    # 키보드 입력
    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_0:
            self.btn0()
        elif e.key() == QtCore.Qt.Key_1:
            self.btn1()
        elif e.key() == QtCore.Qt.Key_2:
            self.btn2()
        elif e.key() == QtCore.Qt.Key_3:
            self.btn3()
        elif e.key() == QtCore.Qt.Key_4:
            self.btn4()
        elif e.key() == QtCore.Qt.Key_5:
            self.btn5()
        elif e.key() == QtCore.Qt.Key_6:
            self.btn6()
        elif e.key() == QtCore.Qt.Key_7:
            self.btn7()
        elif e.key() == QtCore.Qt.Key_8:
            self.btn8()
        elif e.key() == QtCore.Qt.Key_9:
            self.btn9()
        elif e.key() == QtCore.Qt.Key_Period:
            self.btndot()
        elif e.key() == QtCore.Qt.Key_ParenLeft:
            self.btnbracel()
        elif e.key() == QtCore.Qt.Key_ParenRight:
            self.btnbracer()
        elif e.key() == QtCore.Qt.Key_Plus:
            self.btnpls()
        elif e.key() == QtCore.Qt.Key_Minus:
            self.btnmin()
        elif e.key() == QtCore.Qt.Key_Asterisk:
            self.btnmul()
        elif e.key() == QtCore.Qt.Key_Slash:
            self.btndiv()
        elif e.key() == QtCore.Qt.Key_AsciiCircum:
            self.btnsqr()
        elif e.key() == QtCore.Qt.Key_Percent:
            self.btnper()
        elif e.key() == QtCore.Qt.Key_C:
            self.btnclr()
        elif e.key() == QtCore.Qt.Key_Backspace:
            self.btnback()
        elif e.key() == QtCore.Qt.Key_Enter or e.key() == QtCore.Qt.Key_Return or e.key() == QtCore.Qt.Key_Equal:
            self.btnequal()

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

    def btnbracel(self):
        self.formula.append("(")
        self.formula_show.append(" (")
        self.textUpdate()

    def btnbracer(self):
        self.formula.append(")")
        self.formula_show.append(") ")
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
        self.formula.append(" sqrt")
        self.formula.append("(")
        self.formula_show.append(" √")
        self.formula_show.append("(")
        self.textUpdate()

    def btnper(self):
        self.formula.append("/100")
        self.formula_show.append("%")
        self.textUpdate()

    def btnclr(self):
        self.formula.clear()
        self.formula_show.clear()
        self.textUpdate()
        self.koreanText.setText("")

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
            # 계산해서 출력
            self.result = eval(formula)
            self.formula.clear()
            self.formula_show.clear()
            self.formula.append(str(self.result))
            self.formula_show.append(str(self.result))
            self.mainText.setText(str(self.result))
            self.koreanText.setText("")

            # 자연수라면 한글로 표시
            if self.result % 1 == 0:
                text = ""
                remainder = self.result % 10000
                num = 0
                while self.result > 0:
                    text = " " + str(remainder) + CIPHER[num] + text
                    self.result //= 10000
                    remainder = self.result % 10000
                    num += 1

                self.koreanText.setText(text.replace(".0", ""))

        except IndexError:
            pass

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
