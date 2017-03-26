
class Message(object):

    def __init__(self, name, takes_input=False):
        self.name = name
        self.takes_input = takes_input
        self.value = None

    def set_value(self, value):
        """
        Value should be filtered here, like if you want to take the input and multiply it by 10 before it goes out
        By default, it converts the value to an int
        :param value:
        :return:
        """
        
        try:
            value = int(value)
        except ValueError as e:
            print("Bad conversion, error [" + str(e) + "]")

        self.value = value
        return self  # very important for automatic operation generation


commands = [
    Message("Rotate Orange Gripper", True),
    Message("Rotate Green Gripper", True),
    Message("Set W PP Extension", True),
    Message("Set S PP Extension", True),
    Message("Set X PP Extension", True),
    Message("Send Bytes To Bus", True),
    Message("Grip Orange Gripper"),
    Message("Grip Green Gripper"),
    Message("Send Bytes To Payload", True)
]
