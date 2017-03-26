import sys
from time import sleep
from core.gui.gui_base import Ui_gui
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QCoreApplication, QObject, QRunnable, QThread, QThreadPool, pyqtSignal)
from core.message_passing import MessagePasser
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


class Controller(Ui_gui, MessagePasser):

    def __init__(self, dialog, robot_commands):
        Ui_gui.__init__(self)
        MessagePasser.__init__(self)
        self.setupUi(dialog)  # from super
        self.name = "UI"

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

        self.robot_commands = list(robot_commands)

        self.init_debug_table()

    def init_debug_table(self):

        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(["Command", "Input"])

        for robot_command in self.robot_commands:

            target_row = self.tableWidget.rowCount()
            self.tableWidget.insertRow(target_row)

            action_button = QtWidgets.QPushButton(robot_command.name)
            self.tableWidget.setCellWidget(target_row, 0, action_button)

            if robot_command.takes_input:
                user_input = QtWidgets.QLineEdit()
                action_button.clicked.connect(lambda state, r=robot_command, i=user_input: self.add_to_partner(r.set_value(i.text())))
            else:
                user_input = QtWidgets.QLabel("NONE")
                user_input.setAlignment(QtCore.Qt.AlignCenter)
                action_button.clicked.connect(lambda state, r=robot_command: self.add_to_partner(r))

            self.tableWidget.setCellWidget(target_row, 1, user_input)

        self.tableWidget.setVisible(False)
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.setVisible(True)

    def link_values(self, args):
        for arg1 in args:
            for arg2 in args:
                arg1.valueChanged.connect(arg2.setValue)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()

    gui_controller = Controller(dialog)

    dialog.show()
    sys.exit(app.exec_())
