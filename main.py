from PyQt5 import QtCore, QtGui, uic, QtWidgets
import sys


# 메인 윈도우 창
class MainWindow(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = uic.loadUi("GUI.ui", self)
        self.ui.show()


# 앱 실행
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Window = MainWindow(None)
    p = Window.palette()
    p.setColor(Window.backgroundRole(), QtGui.QColor(0, 0, 0))
    Window.setPalette(p)
    Window.show()
    app.exec_()
