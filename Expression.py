class Expression:
    def __init__(self, register, counter):
        self.register = register
        self.counter = counter


class Command:
    def __init__(self, counter):
        self.counter = counter
