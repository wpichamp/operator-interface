
class Message(object):

    def __init__(self, name, takes_input=False):
        self.name = name
        self.takes_input = takes_input


commands = [
    Message("Command 1"),
    Message("Command 2"),
    Message("Command 3")
]
