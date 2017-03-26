
class RobotAction(object):

    def __init__(self, name, callback, takes_input=False):
        self.name = name
        self.takes_input = takes_input
        self.user_input = None
        self.callback = callback
