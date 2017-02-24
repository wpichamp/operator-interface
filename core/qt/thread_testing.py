import sys, time
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtCore import pyqtSignal

app = QtWidgets.QApplication(sys.argv)


class widget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self)

    def appinit(self):
        thread = Worker()
        self.connect(thread, thread.signal, self.testfunc)
        thread.start()

    def testfunc(self, sigstr):
        print(sigstr)


class Worker(QtCore.QThread):

    def __init__(self):
        QtCore.QThread.__init__(self, parent=app)

        self.signal = pyqtSignal()

    def run(self):
        time.sleep(5)
        print("in thread")
        self.emit(self.signal, "hi from thread")


def main():
    w = widget()
    w.show()
    w.appinit()
    sys.exit(app.exec_())

main()

