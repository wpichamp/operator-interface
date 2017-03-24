
class RobotAction(object):

    def __init__(self, name, callback, takes_input=False):
        self.name = name
        self.takes_input = takes_input
        self.user_input = None
        self.callback = callback


class Robot(object):

    def __init__(self):

        self.robot_actions = [
            RobotAction("Rotate Orange Gripper", self.rotate_orange_gripper, True),
            RobotAction("Rotate Green Gripper", self.rotate_green_gripper, True)
        ]

        print(dir(self))

    def rotate_gripper(self, gripper_number, value):
        pass

    def rotate_orange_gripper(self, user_input):
        pass

    def rotate_green_gripper(self, user_input):
        pass

    def grip_orange_gripper(self):
        pass

    def grip_green_gripper(self):
        pass
    
    def set_w_pp_extrusion(self, user_input):
        pass

    def set_x_pp_extrusion(self, user_input):
        pass
    
    def set_s_pp_extrusion(self, user_input):
        pass