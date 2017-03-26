from core.message_passing import MessagePasser


class Robot(MessagePasser):

    def __init__(self):
        MessagePasser.__init__(self)
        self.name = "robot"
