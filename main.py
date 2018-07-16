from PyQt5 import QtCore, QtGui, uic, QtWidgets
import sys


# 메인 윈도우 창
class MainWindow(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = uic.loadUi("GUI.ui", self)
        self.ui.show()

    def btn0(self):
        pass

    def btn1(self):
        pass

    def btn2(self):
        pass

    def btn3(self):
        pass

    def btn4(self):
        pass

    def btn5(self):
        pass

    def btn6(self):
        pass

    def btn7(self):
        pass

    def btn8(self):
        pass

    def btn9(self):
        pass

    def btndot(self):
        pass

    def btnbrace(self):
        pass

    def btnpls(self):
        pass

    def btnmin(self):
        pass

    def btnmul(self):
        pass

    def btndiv(self):
        pass

    def btnsqr(self):
        pass

    def btnroot(self):
        pass

    def btnper(self):
        pass

    def btnclr(self):
        pass

    def btnback(self):
        pass

    def btnequal(self):
        pass


# 앱 실행
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Window = MainWindow(None)
    p = Window.palette()
    p.setColor(Window.backgroundRole(), QtGui.QColor(200, 200, 200))
    Window.setPalette(p)
    Window.show()
    app.exec_()
