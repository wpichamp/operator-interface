import sys
from time import sleep
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QCoreApplication, QObject, QRunnable, QThread, QThreadPool, pyqtSignal)

from gui import Ui_gui


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


class GUI_controller(Ui_gui):

    def __init__(self, dialog):
        Ui_gui.__init__(self)
        self.setupUi(dialog)  # from super

        pp_controls = [
            [self.wpp_target_upper_verticalSlider, self.wpp_target_lower_verticalSlider, self.wpp_target_spinBox],
            [self.wpp_actual_upper_verticalSlider, self.wpp_actual_lower_verticalSlider, self.wpp_actual_spinBox],
            [self.spp_target_upper_verticalSlider, self.spp_target_lower_verticalSlider, self.spp_target_spinBox],
            [self.spp_actual_upper_verticalSlider, self.spp_actual_lower_verticalSlider, self.spp_actual_spinBox],
            [self.xpp_target_upper_verticalSlider, self.xpp_target_lower_verticalSlider, self.xpp_target_spinBox],
            [self.xpp_actual_upper_verticalSlider, self.xpp_actual_lower_verticalSlider, self.xpp_actual_spinBox]
        ]

        gripper_controls = [
            [self.og_target_angle_dial, self.og_target_angle_spinbox],
            [self.gg_target_angle_dial, self.gg_target_angle_spinbox],
            [self.og_actual_angle_dial, self.og_actual_angle_spinbox],
            [self.gg_actual_angle_dial, self.gg_actual_angle_spinbox]
        ]

        all_controls = pp_controls + gripper_controls

        for control_group in all_controls:
            self.link_values(control_group)

        delayed_links = [
            (self.wpp_target_upper_verticalSlider, self.wpp_actual_upper_verticalSlider),
            (self.spp_target_upper_verticalSlider, self.spp_actual_upper_verticalSlider),
            (self.xpp_target_upper_verticalSlider, self.xpp_actual_upper_verticalSlider),
            (self.og_target_angle_dial, self.og_actual_angle_dial),
            (self.gg_target_angle_dial, self.gg_actual_angle_dial)
        ]

        for link in delayed_links:
            self.delayed_value_link(link)


        self.tableWidget.setColumnCount(4)

        self.btn_sell = QtWidgets.QPushButton('Edit')
        self.tableWidget.insertRow(0)
        self.tableWidget.setCellWidget(0, 0, self.btn_sell)

        """
        self.debug_layout = QtWidgets.QGridLayout()

        self.debug_widget = QtWidgets.QWidget()
        self.debug_widget.setLayout(self.debug_layout)

        self.debug_scrollArea.setWidget(self.debug_widget)

        for x in range(100):
            button = QtWidgets.QPushButton("Button " + str(x))

            y_location = 10+(x*20)

            print(y_location)

            button.setGeometry(QtCore.QRect(10, y_location, 70, 20))
            self.debug_layout.addChildWidget(button)
        """




    def delayed_value_link(self, tuple):
        tuple[0].valueChanged.connect(lambda value: self.launch_delay(tuple[1], value))

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

    loop = Loop()

    gui_controller = GUI_controller(dialog)

    gui_controller.make_connection(loop)

    loop.start()

    dialog.show()
    sys.exit(app.exec_())
