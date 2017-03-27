
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


class CommandClass(object):

    rotate_orange_gripper = Message("Rotate Orange Gripper", True)
    rotate_green_gripper = Message("Rotate Green Gripper", True)
    set_w_pp_extension = Message("Set W PP Extension", True)
    set_s_pp_extension = Message("Set S PP Extension", True)
    set_x_pp_extension = Message("Set X PP Extension", True)
    send_bytes_to_bus = Message("Send Bytes To Bus", True)
    grip_orange_gripper = Message("Grip Orange Gripper")
    grip_green_gripper = Message("Grip Green Gripper")
    send_bytes_to_payload = Message("Send Bytes To Payload", True)

    command_list = [
        rotate_orange_gripper,
        rotate_green_gripper,
        set_w_pp_extension,
        set_s_pp_extension,
        set_x_pp_extension,
        send_bytes_to_bus,
        grip_green_gripper,
        grip_orange_gripper,
        send_bytes_to_payload
    ]

command_container = CommandClass()
