from core.message_passing import MessagePasser
from queue import Empty
from random import randint
from messages import Message
from messages import command_container
from time import sleep


class Robot(MessagePasser):

    def __init__(self):
        MessagePasser.__init__(self)
        self.name = "robot"

    def run(self):

        message_count = 0

        while True:

            try:
                # try and get messages from the UI to pass to the robot
                message = self.message_queue.get(timeout=1)
                message_count += 1
                print("In [" + self.name + "] Message: " + message.name)
                if message.takes_input:
                    print("Payload: " + str(message.value))

                if message == command_container.grip_green_gripper:
                    sleep(1)
                    self.add_to_partner(Message("Ungrip Green Gripper"))

            except Empty:
                # try and get commands from the Xbee to pass back to the UI
                if message_count >= 3:
                    message_count = 0
                    print("sending to UI")
                    self.add_to_partner(Message("Hello from robot"))


