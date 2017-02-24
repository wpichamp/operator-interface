from PyQt5 import QtCore

from PyQt5.QtCore import (QCoreApplication, QObject, QRunnable, QThread,
                          QThreadPool, pyqtSignal)

from time import sleep

class Loop(QThread):

    sig = pyqtSignal(int)

    def __init__(self):
        QThread.__init__(self)


    def run(self):

        count = 0

        while True:

            self.sig.emit(count)

            count += 1

            if count > 100:
                count = 0

            sleep(1)