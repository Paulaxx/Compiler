class Expression:
    def __init__(self, register, counter):
        self.register = register
        self.counter = counter


class Command:
    def __init__(self, counter):
        self.counter = counter


class Condition:
    def __init__(self, start, jump, counter, value1, value2, sign):
        self.start = start
        self.jump = jump
        self.counter = counter
        self.value1 = value1
        self.value2 = value2
        self.sign = sign
