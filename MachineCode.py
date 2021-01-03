from SymbolTable import *


class MachineCode:

    def __init__(self):
        self.code = []
        self.command = {'com': "",  'arg1': "", 'arg2': ""}
        # registers:
        self.r1 = {'name': 'a', 'value': -1}
        self.r2 = {'name': 'b', 'value': -1}
        self.r3 = {'name': 'c', 'value': -1}
        self.r4 = {'name': 'd', 'value': -1}
        self.r5 = {'name': 'e', 'value': -1}
        self.r6 = {'name': 'f', 'value': -1}

    def get_register_by_value(self, value):
        if self.r1['value'] == value:
            return self.r1
        elif self.r2['value'] == value:
            return self.r2
        elif self.r3['value'] == value:
            return self.r3
        elif self.r4['value'] == value:
            return self.r4
        elif self.r5['value'] == value:
            return self.r5
        elif self.r6['value'] == value:
            return self.r6
        else:
            return self.r1

    def get_2_registers(self, value1):
        if self.r1['value'] == value1:
            return (self.r1, self.r2)
        elif self.r2['value'] == value1:
            return (self.r2, self.r3)
        elif self.r3['value'] == value1:
            return (self.r3, self.r4)
        elif self.r4['value'] == value1:
            return self.r4, self.r5
        elif self.r5['value'] == value1:
            return self.r5, self.r6
        elif self.r6['value'] == value1:
            return self.r6, self.r1
        else:
            return self.r1, self.r2

    def set_value_to_register(self, r_name, r_value, value):
        if r_value == -1:
            r_value = 0
            command = {'com': "RESET", 'arg1': r_name, 'arg2': ""}
            self.code.append(command)

        if r_value == value:
            return
        if r_value == 0:
            r_value += 1
            command = {'com': "INC", 'arg1': r_name, 'arg2': ""}
            self.code.append(command)
        elif r_value < value:
            while r_value*2 <= value:
                r_value *= 2
                command = {'com': "SHL", 'arg1': r_name, 'arg2': ""}
                self.code.append(command)
                if r_value == value:
                    return
            while r_value+1 <= value:
                r_value += 1
                command = {'com': "INC", 'arg1': r_name, 'arg2': ""}
                self.code.append(command)
                if r_value == value:
                    return
        elif r_value > value:
            while r_value//2 >= value:
                r_value //= 2
                command = {'com': "SHR", 'arg1': r_name, 'arg2': ""}
                self.code.append(command)
                if r_value == value:
                    return
            while r_value-1 >= value:
                r_value -= 1
                command = {'com': "DEC", 'arg1': r_name, 'arg2': ""}
                self.code.append(command)
                if r_value == value:
                    return

    def actualize_register_value(self, name, new_value):
        if name == 'a':
            self.r1['value'] = new_value
        elif name == 'b':
            self.r2['value'] = new_value
        elif name == 'c':
            self.r3['value'] = new_value
        elif name == 'd':
            self.r4['value'] = new_value
        elif name == 'e':
            self.r5['value'] = new_value
        elif name == 'f':
            self.r6['value'] = new_value

    def read(self, variable):
        address = variable[0]['address']
        reg = self.get_register_by_value(address)
        self.set_value_to_register(reg['name'], reg['value'], address)
        command = {'com': "GET", 'arg1': reg['name'], 'arg2': ""}
        self.code.append(command)
        self.actualize_register_value(reg['name'], address)

    def write(self, variable):
        if isinstance(variable, list):
            variable = variable[0]
        if variable['value'] == -1:
            print("Zmienna nie zainicjalizowana")
            sys.exit()
        if variable['is_in_memory'] == 0:
            reg1, reg2 = self.get_2_registers(variable['value'])
            self.set_value_to_register(reg1['name'], reg1['value'], variable['value'])
            self.set_value_to_register(reg2['name'], reg2['value'], variable['address'])
            command = {'com': "STORE", 'arg1': reg1['name'], 'arg2': reg2['name']}
            self.code.append(command)
            command = {'com': "PUT", 'arg1': reg2['name'], 'arg2': ""}
            self.code.append(command)
            self.actualize_register_value(reg1['name'], variable['value'])
            self.actualize_register_value(reg2['name'], variable['address'])
        else:
            reg = self.get_register_by_value(variable['address'])
            self.set_value_to_register(reg['name'], reg['value'], variable['address'])
            command = {'com': "PUT", 'arg1': reg['name'], 'arg2': ""}
            self.code.append(command)
            self.actualize_register_value(reg['name'], variable['address'])