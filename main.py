import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from core.qt.gui_view import Ui_gui_view
from core.oi.xbox import XboxController

class GUI_controller(Ui_gui_view):

    def __init__(self, dialog, gamepad):
        Ui_gui_view.__init__(self)
        self.setupUi(dialog)  # from super

        self.gamepad = gamepad

        # Set up gamepad callback functions
        self.gamepad.setupControlCallback(gamepad.XboxControls.RTHUMBY, self.set_all_extruders)


        # Set up event handlers for UI boundary entities
        self.leftExtruder1_verticalSlider.valueChanged.connect(self.thing)
        self.leftExtruder2_verticalSlider.valueChanged.connect(self.thing)

        self.notEditing = True

    def set_all_extruders(self, value):

        if self.notEditing:
            self.notEditing = False

            value1 = int(value)
            value2 = int(value) * -1

            print("Setting Extruders to: " + str(value1) + ", " + str(value2))

            self.leftExtruder1_verticalSlider.setValue(value1)
            self.leftExtruder2_verticalSlider.setValue(value2)

            """
            self.middleExtruder1_verticalSlider.setValue(value1)
            self.middleExtruder2_verticalSlider.setValue(value2)
            self.rightExtruder1_verticalSlider.setValue(value1)
            self.rightExtruder2_verticalSlider.setValue(value2)
            """

            self.notEditing = True

    def thing(self):
        pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()

    gamepad = XboxController(None, deadzone=10, scale=100, invertYAxis=True)

    gui_controller = GUI_controller(dialog, gamepad)

    gamepad.finished.connect(app.exit)
    gamepad.start()

    dialog.show()
    sys.exit(app.exec_())
