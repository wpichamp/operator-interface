import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QCoreApplication, QObject, QRunnable, QThread,
                          QThreadPool, pyqtSignal)
from core.qt.gui_view import Ui_gui_view
from core.oi.xbox import XboxController

class GUI_controller(Ui_gui_view):

    def __init__(self, dialog, gamepad):
        Ui_gui_view.__init__(self)
        self.setupUi(dialog)  # from super

        self.gamepad = gamepad

        controls_to_sliders = {
            gamepad.XboxControls.RTHUMBY: self.rightStickY_verticalSlider,
            gamepad.XboxControls.RTHUMBX: self.rightStickX_verticalSlider,
            gamepad.XboxControls.LTHUMBY: self.leftStickY_verticalSlider,
            gamepad.XboxControls.LTHUMBX: self.leftStickX_verticalSlider,
            gamepad.XboxControls.TRIGGER: self.leftTrigger_verticalSlide
        }

        controls_to_buttons = {
            gamepad.XboxControls.A: self.a_pushButton,
            gamepad.XboxControls.B: self.b_pushButton,
            gamepad.XboxControls.X: self.x_pushButton,
            gamepad.XboxControls.Y: self.y_pushButton,
            gamepad.XboxControls.RB: self.rightBumper_pushButton,
            gamepad.XboxControls.LB: self.leftBumper_pushButton,
            gamepad.XboxControls.LEFTTHUMB: self.leftStrick_pushButton,
            gamepad.XboxControls.RIGHTTHUMB: self.rightStick_pushButton,
            gamepad.XboxControls.START: self.start_pushButton,
            gamepad.XboxControls.BACK: self.back_pushButton,
        }

        for gamepad_signal in controls_to_sliders.keys():
            self.connect_gamepad_signal(gamepad_signal, self.setSlider(controls_to_sliders[gamepad_signal]))

        for gamepad_signal in controls_to_buttons.keys():
            self.connect_gamepad_signal(gamepad_signal, self.setButton(controls_to_buttons[gamepad_signal]))

    def setSlider(self, slider):
        return lambda value: slider.setValue(value)

    def setButton(self, button):
        return lambda value: button.setFlat(value)

    def connect_gamepad_signal(self, source, function):
        self.gamepad.signals[source].connect(function)




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()

    gamepad_thread = XboxController(None, deadzone=10, scale=100, invertYAxis=True)

    gui_controller = GUI_controller(dialog, gamepad_thread)

    gamepad_thread.start()

    dialog.show()
    sys.exit(app.exec_())
