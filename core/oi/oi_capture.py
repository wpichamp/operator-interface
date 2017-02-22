from PyQt5 import QtCore, QtGui, QtWidgets
import pygame


class OI_capture(QtCore.QThread):

    def __init__(self):

        QtCore.QThread.__init__(self)

        self.left_stick_x = 0
        self.left_stick_y = 0
        self.right_stick_x = 0
        self.right_stick_y = 0

        self.a_button = 0
        self.b_button = 0
        self.x_button = 0
        self.y_button = 0

        self.left_bumper = 0
        self.right_bumper = 0

        self.back_button = 0
        self.start_button = 0

        self.left_stick_button = 0
        self.right_stick_button = 0

    def run(self):

        pygame.init()

        # Initialize the joysticks
        pygame.joystick.init()

        # Get the number of joystick devices attached to the computer
        joystick_count = pygame.joystick.get_count()

        if joystick_count is 0:
            print("Joystick removed, exiting program")
            capturing = False

        joystick = pygame.joystick.Joystick(0)
        joystick.init()

        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                capturing = False  # Flag that we are done so we exit this loop

        self.left_stick_x = joystick.get_axis(0)
        self.left_stick_y = joystick.get_axis(1)
        self.right_stick_x = joystick.get_axis(3)
        self.right_stick_y = joystick.get_axis(4)

        self.a_button = joystick.get_button(0)
        self.b_button = joystick.get_button(1)
        self.x_button = joystick.get_button(2)
        self.y_button = joystick.get_button(3)

        self.left_bumper = joystick.get_button(4)
        self.right_bumper = joystick.get_button(5)

        self.back_button = joystick.get_button(6)
        self.start_button = joystick.get_button(7)

        self.left_stick_button = joystick.get_button(8)
        self.right_stick_button = joystick.get_button(9)
