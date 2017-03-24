import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QCoreApplication, QObject, QRunnable, QThread, QThreadPool, pyqtSignal)
from core.gui.gui_controller import Controller
from core.robot.robot_controller import Robot

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()

    champ = Robot()

    gui = Controller(dialog, champ.robot_actions)

    dialog.show()
    sys.exit(app.exec_())
