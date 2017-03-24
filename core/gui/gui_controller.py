import sys
from time import sleep
from core.gui.gui_base import Ui_gui
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QCoreApplication, QObject, QRunnable, QThread, QThreadPool, pyqtSignal)
from functools import partial

class Loop(QThread):

    signal = pyqtSignal(str)

    def __init__(self):
        QThread.__init__(self)

    def run(self):
        count = 0
        while True:

            if count % 10:
                self.signal.emit("[Debug Message]: " + str(count))
            else:
                self.signal.emit("[Error Message]: " + str(count))

            count += 1
            if count > 100:
                count = 0
            sleep(.5)


class DelayThread(QThread):

    signal = pyqtSignal(int)

    def __init__(self, value):
        QThread.__init__(self)
        self.value = value

    def run(self):
        sleep(.2)
        self.signal.emit(self.value)


class Controller(Ui_gui):

    def __init__(self, dialog, robot_actions):
        Ui_gui.__init__(self)
        self.setupUi(dialog)  # from super

        loop = Loop()
        self.make_connection(loop)
        loop.start()

        linked_controls = [
            [self.wpp_target_upper_verticalSlider, self.wpp_target_lower_verticalSlider, self.wpp_target_spinBox],
            [self.wpp_actual_upper_verticalSlider, self.wpp_actual_lower_verticalSlider, self.wpp_actual_spinBox],
            [self.spp_target_upper_verticalSlider, self.spp_target_lower_verticalSlider, self.spp_target_spinBox],
            [self.spp_actual_upper_verticalSlider, self.spp_actual_lower_verticalSlider, self.spp_actual_spinBox],
            [self.xpp_target_upper_verticalSlider, self.xpp_target_lower_verticalSlider, self.xpp_target_spinBox],
            [self.xpp_actual_upper_verticalSlider, self.xpp_actual_lower_verticalSlider, self.xpp_actual_spinBox],
            [self.og_target_angle_dial, self.og_target_angle_spinbox],
            [self.gg_target_angle_dial, self.gg_target_angle_spinbox],
            [self.og_actual_angle_dial, self.og_actual_angle_spinbox],
            [self.gg_actual_angle_dial, self.gg_actual_angle_spinbox],
            [self.speedfactor_horizontalSlider, self.speedfactor_spinBox]
        ]

        for control_group in linked_controls:
            self.link_values(control_group)

        delayed_links = [
            (self.wpp_target_upper_verticalSlider, self.wpp_actual_upper_verticalSlider),
            (self.spp_target_upper_verticalSlider, self.spp_actual_upper_verticalSlider),
            (self.xpp_target_upper_verticalSlider, self.xpp_actual_upper_verticalSlider),
            (self.og_target_angle_dial, self.og_actual_angle_dial),
            (self.gg_target_angle_dial, self.gg_actual_angle_dial)
        ]

        for link in delayed_links:
            source = link[0]
            target = link[1]
            self.delayed_value_link(source, target)

        self.robot_actions = robot_actions

        self.init_debug_table()

    def init_debug_table(self):

        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(["Command", "Input"])

        for action in self.robot_actions:

            target_row = self.tableWidget.rowCount()
            self.tableWidget.insertRow(target_row)

            action_button = QtWidgets.QPushButton(action.name)
            self.tableWidget.setCellWidget(target_row, 0, action_button)

            if action.takes_input:
                user_input = QtWidgets.QLineEdit()
                self.tableWidget.setCellWidget(target_row, 1, user_input)
            else:
                user_input = QtWidgets.QLabel("NONE")
                user_input.setAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.setCellWidget(target_row, 1, user_input)

            action_button.clicked.connect(partial(action.callback, user_input))

    def delayed_value_link(self, source, target):
        source.valueChanged.connect(lambda value: self.launch_delay(target, value))

    def launch_delay(self, target, value):
        self.delay_thread = DelayThread(value)
        self.delay_thread.signal.connect(target.setValue)
        self.delay_thread.start()

    def link_values(self, args):
        for arg1 in args:
            for arg2 in args:
                arg1.valueChanged.connect(arg2.setValue)

    def make_connection(self, sig_object):
        sig_object.signal.connect(self.add_text)

    def add_text(self, text):
        self.plainTextEdit.appendPlainText(text)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()

    gui_controller = Controller(dialog)

    dialog.show()
    sys.exit(app.exec_())
