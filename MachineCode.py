from SymbolTable import *
from Expression import *


class MachineCode:

    def __init__(self):
        self.code = []
        self.command = {'com': "", 'arg1': "", 'arg2': ""}
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
            return self.r1, self.r2
        elif self.r2['value'] == value1:
            return self.r2, self.r3
        elif self.r3['value'] == value1:
            return self.r3, self.r4
        elif self.r4['value'] == value1:
            return self.r4, self.r5
        elif self.r5['value'] == value1:
            return self.r5, self.r6
        elif self.r6['value'] == value1:
            return self.r6, self.r1
        else:
            return self.r1, self.r2

    def get_3_registers(self, value1):
        if self.r1['value'] == value1:
            return self.r1, self.r2, self.r3
        elif self.r2['value'] == value1:
            return self.r2, self.r3, self.r4
        elif self.r3['value'] == value1:
            return self.r3, self.r4, self.r5
        elif self.r4['value'] == value1:
            return self.r4, self.r5, self.r6
        elif self.r5['value'] == value1:
            return self.r5, self.r6, self.r1
        elif self.r6['value'] == value1:
            return self.r6, self.r1, self.r2
        else:
            return self.r1, self.r2, self.r3

    def get_4_registers(self, value1):
        if self.r1['value'] == value1:
            return self.r1, self.r2, self.r3, self.r4
        elif self.r2['value'] == value1:
            return self.r2, self.r3, self.r4, self.r5
        elif self.r3['value'] == value1:
            return self.r3, self.r4, self.r5, self.r6
        elif self.r4['value'] == value1:
            return self.r4, self.r5, self.r6, self.r1
        elif self.r5['value'] == value1:
            return self.r5, self.r6, self.r1, self.r2
        elif self.r6['value'] == value1:
            return self.r6, self.r1, self.r2, self.r3
        else:
            return self.r1, self.r2, self.r3, self.r4

    def get_register_diff(self, reg):
        if self.r1['name'] != reg:
            return self.r1
        elif self.r2['name'] != reg:
            return self.r2
        elif self.r3['name'] != reg:
            return self.r3
        elif self.r4['name'] != reg:
            return self.r4
        elif self.r5['name'] != reg:
            return self.r5
        else:
            return self.r6

    def get_2_registers_diff(self, reg):
        if self.r1['name'] != reg and self.r2['name'] != reg:
            return self.r1, self.r2
        elif self.r1['name'] != reg and self.r3['name'] != reg:
            return self.r1, self.r3
        elif self.r1['name'] != reg and self.r4['name'] != reg:
            return self.r1, self.r4
        elif self.r1['name'] != reg and self.r5['name'] != reg:
            return self.r1, self.r5
        elif self.r1['name'] != reg and self.r6['name'] != reg:
            return self.r1, self.r6
        elif self.r2['name'] != reg and self.r3['name'] != reg:
            return self.r2, self.r3
        elif self.r2['name'] != reg and self.r4['name'] != reg:
            return self.r2, self.r4
        elif self.r2['name'] != reg and self.r5['name'] != reg:
            return self.r2, self.r5
        elif self.r2['name'] != reg and self.r6['name'] != reg:
            return self.r2, self.r6
        elif self.r3['name'] != reg and self.r4['name'] != reg:
            return self.r3, self.r4
        elif self.r3['name'] != reg and self.r5['name'] != reg:
            return self.r3, self.r5
        elif self.r3['name'] != reg and self.r6['name'] != reg:
            return self.r3, self.r6
        elif self.r4['name'] != reg and self.r5['name'] != reg:
            return self.r4, self.r5
        elif self.r4['name'] != reg and self.r6['name'] != reg:
            return self.r4, self.r6
        else:
            return self.r5, self.r6

    def set_value_to_register(self, r_name, r_value, value):
        value = int(value)
        r_value = -1
        binary_rep = [int(x) for x in bin(value)[2:]]

        if r_value == -1:
            r_value = 0
            command = {'com': "RESET", 'arg1': r_name, 'arg2': ""}
            self.code.append(command)

        for i in binary_rep:
            command = {'com': "SHL", 'arg1': r_name, 'arg2': ""}
            self.code.append(command)
            if i == 1:
                command = {'com': "INC", 'arg1': r_name, 'arg2': ""}
                self.code.append(command)

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
        if isinstance(variable, list):
            variable = variable[0]
        if variable['value'] == -2:
            reg1, reg2 = self.get_2_registers(variable['address'])
            self.set_value_to_register(reg1['name'], reg2['value'], variable['address'])
            self.actualize_register_value(reg1['name'], variable['address'])

            self.set_value_to_register(reg2['name'], reg2['value'], variable['name'])
            command = {'com': "LOAD", 'arg1': reg2['name'], 'arg2': reg2['name']}
            self.code.append(command)
            self.actualize_register_value(reg2['name'], -1)
            command = {'com': "ADD", 'arg1': reg1['name'], 'arg2': reg2['name']}
            self.code.append(command)
            command = {'com': "GET", 'arg1': reg1['name'], 'arg2': ""}
            self.code.append(command)
        else:
            address = variable['address']
            # address = variable['address']
            reg = self.get_register_by_value(address)
            self.set_value_to_register(reg['name'], reg['value'], address)
            command = {'com': "GET", 'arg1': reg['name'], 'arg2': ""}
            self.code.append(command)
            self.actualize_register_value(reg['name'], address)

    def write(self, variable):
        if isinstance(variable, list):
            variable = variable[0]
        if variable['value'] == -1 and variable['table'] == 0 and variable['iterator'] == 0:
            print("Zmienna nie zainicjalizowana")
            sys.exit()

        if variable['value'] == -2:
            reg1, reg2 = self.get_2_registers(variable['address'])
            if variable['address'] == -1:
                self.set_value_to_register(reg2['name'], reg2['value'], int(variable['name']))
                command = {'com': "LOAD", 'arg1': reg2['name'], 'arg2': reg2['name']}
                self.code.append(command)
                self.actualize_register_value(reg2['name'], -1)
                command = {'com': "DEC", 'arg1': reg2['name'], 'arg2': ""}
                self.code.append(command)
                command = {'com': "PUT", 'arg1': reg2['name'], 'arg2': ""}
                self.code.append(command)
            elif variable['address'] < 0:
                self.set_value_to_register(reg1['name'], reg1['value'], variable['name'])
                command = {'com': "LOAD", 'arg1': reg1['name'], 'arg2': reg1['name']}
                self.code.append(command)
                self.set_value_to_register(reg2['name'], reg2['value'], abs(int(variable['address'])))
                command = {'com': "SUB", 'arg1': reg1['name'], 'arg2': reg2['name']}
                self.code.append(command)
                command = {'com': "PUT", 'arg1': reg1['name'], 'arg2': ""}
                self.code.append(command)
                self.actualize_register_value(reg1['name'], -1)
                self.actualize_register_value(reg2['name'], abs(int(variable['address'])))
            else:
                self.set_value_to_register(reg1['name'], reg2['value'], variable['address'])
                self.actualize_register_value(reg1['name'], variable['address'])

                self.set_value_to_register(reg2['name'], reg2['value'], int(variable['name']))
                command = {'com': "LOAD", 'arg1': reg2['name'], 'arg2': reg2['name']}
                self.code.append(command)
                self.actualize_register_value(reg2['name'], -1)
                command = {'com': "ADD", 'arg1': reg1['name'], 'arg2': reg2['name']}
                self.code.append(command)
                command = {'com': "PUT", 'arg1': reg1['name'], 'arg2': ""}
                self.code.append(command)
        elif variable['only_value'] == 1 and variable['is_in_memory'] == 0:
            reg1, reg2 = self.get_2_registers(variable['value'])
            self.set_value_to_register(reg1['name'], reg1['value'], variable['value'])
            self.set_value_to_register(reg2['name'], reg2['value'], variable['address'])
            command = {'com': "STORE", 'arg1': reg1['name'], 'arg2': reg2['name']}
            self.code.append(command)
            command = {'com': "PUT", 'arg1': reg2['name'], 'arg2': ""}
            self.code.append(command)
            self.actualize_register_value(reg1['name'], -1)
            self.actualize_register_value(reg2['name'], -1)
        elif variable['only_value'] == 1 and variable['is_in_memory'] == 1:
            reg = self.get_register_by_value(variable['address'])
            self.set_value_to_register(reg['name'], reg['value'], variable['address'])
            command = {'com': "PUT", 'arg1': reg['name'], 'arg2': ""}
            self.code.append(command)
            self.actualize_register_value(reg['name'], variable['address'])
        elif variable['only_value'] == 0:
            reg = self.get_register_by_value(variable['address'])
            self.set_value_to_register(reg['name'], reg['value'], variable['address'])
            command = {'com': "PUT", 'arg1': reg['name'], 'arg2': ""}
            self.code.append(command)
            self.actualize_register_value(reg['name'], variable['address'])

    def expression_1(self, variable):
        if isinstance(variable, list):
            variable = variable[0]
        if variable['value'] == -1 and variable['table'] == 0 and variable['iterator'] == 0:
            print("Zmienna ", variable['name'], " nie zainicjalizowana")
            sys.exit()

        if variable['value'] == -2:
            reg1, reg2 = self.get_2_registers(variable['address'])

            if variable['address'] == -1:
                self.set_value_to_register(reg2['name'], reg2['value'], variable['name'])
                command = {'com': "LOAD", 'arg1': reg2['name'], 'arg2': reg2['name']}
                self.code.append(command)
                self.actualize_register_value(reg2['name'], -1)
                command = {'com': "DEC", 'arg1': reg2['name'], 'arg2': ""}
                self.code.append(command)
                command = {'com': "LOAD", 'arg1': reg2['name'], 'arg2': reg2['name']}
                self.code.append(command)
                return reg2
            else:
                self.set_value_to_register(reg1['name'], reg2['value'], variable['address'])
                self.actualize_register_value(reg1['name'], variable['address'])

                self.set_value_to_register(reg2['name'], reg2['value'], variable['name'])
                command = {'com': "LOAD", 'arg1': reg2['name'], 'arg2': reg2['name']}
                self.code.append(command)
                self.actualize_register_value(reg2['name'], -1)
                command = {'com': "ADD", 'arg1': reg1['name'], 'arg2': reg2['name']}
                self.code.append(command)
                command = {'com': "LOAD", 'arg1': reg1['name'], 'arg2': reg1['name']}
                self.code.append(command)
                return reg1
        elif variable['only_value'] == 1:
            value = variable['value']
            reg = self.get_register_by_value(value)
            self.set_value_to_register(reg['name'], reg['value'], value)
            self.actualize_register_value(reg['name'], value)
            return reg
        else:
            if variable['value'] == -1 and variable['table'] == 0 and variable['iterator'] == 0:
                print("Zmienna ", variable['name'], " nie zainicjalizowana")
                sys.exit()
            else:
                address = variable['address']
                reg = self.get_register_by_value(address)
                self.set_value_to_register(reg['name'], reg['value'], address)
                self.actualize_register_value(reg['name'], address)
                command = {'com': "LOAD", 'arg1': reg['name'], 'arg2': reg['name']}
                self.code.append(command)
                self.actualize_register_value(reg['name'], -1)
                return reg

    def expression_plus_minus(self, var1, var2, sign):
        if isinstance(var1, list):
            var1 = var1[0]
        if isinstance(var2, list):
            var2 = var2[0]
        if var1['value'] == -1 and var1['table'] == 0 and var1['iterator'] == 0:
            print("Zmienna ", var1['name'], " nie zainicjalizowana")
            sys.exit()
        elif var2['value'] == -1 and var2['table'] == 0 and var2['iterator'] == 0:
            print("Zmienna ", var2['name'], " nie zainicjalizowana")
            sys.exit()

        if var1['only_value'] == 1 and var2['only_value'] == 1:
            if sign == '+':
                result = var1['value'] + var2['value']
            elif sign == '-':
                result = max(var1['value'] - var2['value'], 0)
            reg = self.get_register_by_value(result)
            self.set_value_to_register(reg['name'], reg['value'], result)
            self.actualize_register_value(reg['name'], result)
            return reg
        elif var1['value'] == -2 and var2['only_value'] == 1:
            reg1, reg2 = self.get_2_registers(var1['address'])
            self.set_value_to_register(reg1['name'], reg1['value'], var1['address'])
            self.actualize_register_value(reg1['name'], var1['address'])
            self.set_value_to_register(reg2['name'], reg2['value'], var1['name'])
            command = {'com': "LOAD", 'arg1': reg2['name'], 'arg2': reg2['name']}
            self.code.append(command)
            self.actualize_register_value(reg2['name'], -1)
            command = {'com': "ADD", 'arg1': reg1['name'], 'arg2': reg2['name']}
            self.code.append(command)
            command = {'com': "LOAD", 'arg1': reg1['name'], 'arg2': reg1['name']}
            self.code.append(command)

            self.set_value_to_register(reg2['name'], reg2['value'], var2['value'])
            self.actualize_register_value(reg2['name'], var2['value'])
            if sign == '+':
                command = {'com': "ADD", 'arg1': reg1['name'], 'arg2': reg2['name']}
            elif sign == '-':
                command = {'com': "SUB", 'arg1': reg1['name'], 'arg2': reg2['name']}
            self.code.append(command)
            self.actualize_register_value(reg1['name'], -1)
            return reg1

        elif var1['value'] == -2 and var2['only_value'] == 0:
            reg1, reg2 = self.get_2_registers(var1['address'])
            self.set_value_to_register(reg1['name'], reg1['value'], var1['address'])
            self.actualize_register_value(reg1['name'], var1['address'])
            self.set_value_to_register(reg2['name'], reg2['value'], var1['name'])
            command = {'com': "LOAD", 'arg1': reg2['name'], 'arg2': reg2['name']}
            self.code.append(command)
            self.actualize_register_value(reg2['name'], -1)
            command = {'com': "ADD", 'arg1': reg1['name'], 'arg2': reg2['name']}
            self.code.append(command)
            command = {'com': "LOAD", 'arg1': reg1['name'], 'arg2': reg1['name']}
            self.code.append(command)

            address2 = var2['address']
            self.set_value_to_register(reg2['name'], reg2['value'], address2)
            command = {'com': "LOAD", 'arg1': reg2['name'], 'arg2': reg2['name']}
            self.code.append(command)
            self.actualize_register_value(reg2['name'], -1)
            if sign == '+':
                command = {'com': "ADD", 'arg1': reg1['name'], 'arg2': reg2['name']}
            elif sign == '-':
                command = {'com': "SUB", 'arg1': reg1['name'], 'arg2': reg2['name']}
            self.code.append(command)
            self.actualize_register_value(reg1['name'], -1)
            return reg1

        elif var1['only_value'] == 1 and var2['value'] == -2:
            reg1, reg2 = self.get_2_registers(var2['address'])
            self.set_value_to_register(reg1['name'], reg1['value'], var2['address'])
            self.actualize_register_value(reg1['name'], var2['address'])
            self.set_value_to_register(reg2['name'], reg2['value'], var2['name'])
            command = {'com': "LOAD", 'arg1': reg2['name'], 'arg2': reg2['name']}
            self.code.append(command)
            self.actualize_register_value(reg2['name'], -1)
            command = {'com': "ADD", 'arg1': reg1['name'], 'arg2': reg2['name']}
            self.code.append(command)
            command = {'com': "LOAD", 'arg1': reg1['name'], 'arg2': reg1['name']}
            self.code.append(command)

            self.set_value_to_register(reg2['name'], reg2['value'], var1['value'])
            self.actualize_register_value(reg2['name'], var1['value'])
            if sign == '+':
                command = {'com': "ADD", 'arg1': reg2['name'], 'arg2': reg1['name']}
            elif sign == '-':
                command = {'com': "SUB", 'arg1': reg2['name'], 'arg2': reg1['name']}
            self.code.append(command)
            self.actualize_register_value(reg2['name'], -1)
            return reg2


        elif var1['only_value'] == 0 and var2['value'] == -2:
            reg1, reg2 = self.get_2_registers(var2['address'])
            self.set_value_to_register(reg1['name'], reg1['value'], var2['address'])
            self.actualize_register_value(reg1['name'], var2['address'])
            self.set_value_to_register(reg2['name'], reg2['value'], var2['name'])
            command = {'com': "LOAD", 'arg1': reg2['name'], 'arg2': reg2['name']}
            self.code.append(command)
            self.actualize_register_value(reg2['name'], -1)
            command = {'com': "ADD", 'arg1': reg1['name'], 'arg2': reg2['name']}
            self.code.append(command)
            command = {'com': "LOAD", 'arg1': reg1['name'], 'arg2': reg1['name']}
            self.code.append(command)

            self.set_value_to_register(reg2['name'], reg2['value'], var1['address'])
            command = {'com': "LOAD", 'arg1': reg2['name'], 'arg2': reg2['name']}
            self.code.append(command)

            if sign == '+':
                command = {'com': "ADD", 'arg1': reg2['name'], 'arg2': reg1['name']}
            elif sign == '-':
                command = {'com': "SUB", 'arg1': reg2['name'], 'arg2': reg1['name']}
            self.code.append(command)
            self.actualize_register_value(reg2['name'], -1)
            return reg2

        elif var1['value'] == -2 and var2['value'] == -2:
            reg1, reg2, reg3 = self.get_3_registers(var1['address'])
            self.set_value_to_register(reg1['name'], reg1['value'], var1['address'])
            self.actualize_register_value(reg1['name'], var1['address'])
            self.set_value_to_register(reg2['name'], reg2['value'], var1['name'])
            command = {'com': "LOAD", 'arg1': reg2['name'], 'arg2': reg2['name']}
            self.code.append(command)
            self.actualize_register_value(reg2['name'], -1)
            command = {'com': "ADD", 'arg1': reg1['name'], 'arg2': reg2['name']}
            self.code.append(command)
            command = {'com': "LOAD", 'arg1': reg1['name'], 'arg2': reg1['name']}
            self.code.append(command)

            self.set_value_to_register(reg2['name'], reg2['value'], var2['address'])
            self.actualize_register_value(reg2['name'], var2['address'])
            self.set_value_to_register(reg3['name'], reg3['value'], var2['name'])
            command = {'com': "LOAD", 'arg1': reg3['name'], 'arg2': reg3['name']}
            self.code.append(command)
            self.actualize_register_value(reg3['name'], -1)
            command = {'com': "ADD", 'arg1': reg2['name'], 'arg2': reg3['name']}
            self.code.append(command)
            command = {'com': "LOAD", 'arg1': reg2['name'], 'arg2': reg2['name']}
            self.code.append(command)

            if sign == '+':
                command = {'com': "ADD", 'arg1': reg1['name'], 'arg2': reg2['name']}
            elif sign == '-':
                command = {'com': "SUB", 'arg1': reg1['name'], 'arg2': reg2['name']}
            self.code.append(command)
            self.actualize_register_value(reg1['name'], -1)
            return reg1


        elif var1['only_value'] == 1 and var2['only_value'] == 0:
            value1 = var1['value']
            reg1, reg2 = self.get_2_registers(value1)
            self.set_value_to_register(reg1['name'], reg1['value'], value1)
            self.actualize_register_value(reg1['name'], value1)

            address2 = var2['address']
            self.set_value_to_register(reg2['name'], reg2['value'], address2)
            self.actualize_register_value(reg2['name'], address2)
            command = {'com': "LOAD", 'arg1': reg2['name'], 'arg2': reg2['name']}
            self.code.append(command)
            self.actualize_register_value(reg2['name'], -1)

            if sign == '+':
                command = {'com': "ADD", 'arg1': reg1['name'], 'arg2': reg2['name']}
            elif sign == '-':
                command = {'com': "SUB", 'arg1': reg1['name'], 'arg2': reg2['name']}
            self.code.append(command)
            self.actualize_register_value(reg1['name'], -1)
            return reg1
        elif var1['only_value'] == 0 and var2['only_value'] == 1:
            value2 = var2['value']
            reg2, reg1 = self.get_2_registers(value2)
            self.set_value_to_register(reg2['name'], reg2['value'], value2)
            self.actualize_register_value(reg2['name'], value2)

            address1 = var1['address']
            self.set_value_to_register(reg1['name'], reg1['value'], address1)
            self.actualize_register_value(reg1['name'], address1)
            command = {'com': "LOAD", 'arg1': reg1['name'], 'arg2': reg1['name']}
            self.code.append(command)
            self.actualize_register_value(reg1['name'], -1)

            if sign == '+':
                command = {'com': "ADD", 'arg1': reg1['name'], 'arg2': reg2['name']}
            elif sign == '-':
                command = {'com': "SUB", 'arg1': reg1['name'], 'arg2': reg2['name']}
            self.code.append(command)
            self.actualize_register_value(reg1['name'], -1)
            return reg1
        else:
            address1 = var1['address']
            reg1, reg2 = self.get_2_registers(address1)

            self.set_value_to_register(reg1['name'], reg1['value'], address1)
            self.actualize_register_value(reg1['name'], address1)
            command = {'com': "LOAD", 'arg1': reg1['name'], 'arg2': reg1['name']}
            self.code.append(command)
            self.actualize_register_value(reg1['name'], -1)

            address2 = var2['address']
            self.set_value_to_register(reg2['name'], reg2['value'], address2)
            self.actualize_register_value(reg2['name'], address2)
            command = {'com': "LOAD", 'arg1': reg2['name'], 'arg2': reg2['name']}
            self.code.append(command)
            self.actualize_register_value(reg2['name'], -1)

            if sign == '+':
                command = {'com': "ADD", 'arg1': reg1['name'], 'arg2': reg2['name']}
            elif sign == '-':
                command = {'com': "SUB", 'arg1': reg1['name'], 'arg2': reg2['name']}
            self.code.append(command)
            self.actualize_register_value(reg1['name'], -1)
            return reg1

    def expression_times(self, var1, var2):
        if isinstance(var1, list):
            var1 = var1[0]
        if isinstance(var2, list):
            var2 = var2[0]
        if var1['value'] == -1 and var1['table'] == 0 and var1['iterator'] == 0:
            print("Zmienna ", var1['name'], " nie zainicjalizowana")
            sys.exit()
        elif var2['value'] == -1 and var2['table'] == 0 and var2['iterator'] == 0:
            print("Zmienna ", var2['name'], " nie zainicjalizowana")
            sys.exit()

        reg1, reg2, reg3 = self.get_3_registers(0)
        if var1['only_value'] == 1:
            value = var1['value']
            self.set_value_to_register(reg1['name'], reg1['value'], value)
            self.actualize_register_value(reg1['name'], value)
        elif var1['only_value'] == 0:
            address = var1['address']
            self.set_value_to_register(reg1['name'], reg1['value'], address)
            command = {'com': "LOAD", 'arg1': reg1['name'], 'arg2': reg1['name']}
            self.code.append(command)
            self.actualize_register_value(reg1['name'], -1)
        elif var1['only_value'] == -2:
            self.set_value_to_register(reg1['name'], reg1['value'], var1['address'])
            self.actualize_register_value(reg1['name'], -1)
            self.set_value_to_register(reg2['name'], reg2['value'], var1['name'])
            command = {'com': "LOAD", 'arg1': reg2['name'], 'arg2': reg2['name']}
            self.code.append(command)
            self.actualize_register_value(reg2['name'], -1)
            command = {'com': "ADD", 'arg1': reg1['name'], 'arg2': reg2['name']}
            self.code.append(command)
            command = {'com': "LOAD", 'arg1': reg1['name'], 'arg2': reg1['name']}
            self.code.append(command)

        if var2['only_value'] == 1:
            value = var2['value']
            self.set_value_to_register(reg2['name'], reg2['value'], value)
            self.actualize_register_value(reg2['name'], value)
        elif var2['only_value'] == 0:
            address = var2['address']
            self.set_value_to_register(reg2['name'], reg2['value'], address)
            command = {'com': "LOAD", 'arg1': reg2['name'], 'arg2': reg2['name']}
            self.code.append(command)
            self.actualize_register_value(reg2['name'], -1)
        elif var2['only_value'] == -2:
            if var2['address'] < 0:
                self.set_value_to_register(reg2['name'], reg2['value'], var2['name'])
                command = {'com': "LOAD", 'arg1': reg2['name'], 'arg2': reg2['name']}
                self.code.append(command)
                self.set_value_to_register(reg3['name'], reg3['value'], abs(int(var2['address'])))
                command = {'com': "SUB", 'arg1': reg2['name'], 'arg2': reg3['name']}
                self.code.append(command)
                command = {'com': "LOAD", 'arg1': reg2['name'], 'arg2': reg2['name']}
                self.code.append(command)
                self.actualize_register_value(reg2['name'], -1)
                self.actualize_register_value(reg3['name'], abs(int(var2['address'])))
            else:
                self.set_value_to_register(reg2['name'], reg2['value'], var2['address'])
                self.actualize_register_value(reg2['name'], -1)
                self.set_value_to_register(reg3['name'], reg3['value'], var2['name'])
                command = {'com': "LOAD", 'arg1': reg3['name'], 'arg2': reg3['name']}
                self.code.append(command)
                self.actualize_register_value(reg3['name'], -1)
                command = {'com': "ADD", 'arg1': reg2['name'], 'arg2': reg3['name']}
                self.code.append(command)
                command = {'com': "LOAD", 'arg1': reg2['name'], 'arg2': reg2['name']}
                self.code.append(command)

        self.set_value_to_register(reg3['name'], reg3['value'], 0)
        command = {'com': "JODD", 'arg1': reg2['name'], 'arg2': str(5)}
        self.code.append(command)
        command = {'com': "SHL", 'arg1': reg1['name'], 'arg2': ""}
        self.code.append(command)
        command = {'com': "SHR", 'arg1': reg2['name'], 'arg2': ""}
        self.code.append(command)
        command = {'com': "JZERO", 'arg1': reg2['name'], 'arg2': str(4)}
        self.code.append(command)
        command = {'com': "JUMP", 'arg1': str(-4), 'arg2': ""}
        self.code.append(command)
        command = {'com': "ADD", 'arg1': reg3['name'], 'arg2': reg1['name']}
        self.code.append(command)
        command = {'com': "JUMP", 'arg1': str(-5), 'arg2': ""}
        self.code.append(command)
        return reg3

    def expression_divide(self, var1, var2):
        if isinstance(var1, list):
            var1 = var1[0]
        if isinstance(var2, list):
            var2 = var2[0]
        if var1['value'] == -1 and var1['table'] == 0 and var1['iterator'] == 0:
            print("Zmienna ", var1['name'], " nie zainicjalizowana")
            sys.exit()
        elif var2['value'] == -1 and var2['table'] == 0 and var2['iterator'] == 0:
            print("Zmienna ", var2['name'], " nie zainicjalizowana")
            sys.exit()

        if var1['only_value'] == 1 and var2['only_value'] == 1:
            if var2['value'] == 0:
                result = 0
            else:
                result = var1['value'] // var2['value']
            reg = self.get_register_by_value(result)
            self.set_value_to_register(reg['name'], reg['value'], result)
            self.actualize_register_value(reg['name'], result)
            return reg
        elif var1['only_value'] == 1 and var2['only_value'] == 0:
            if var1['value'] == 0:
                reg = self.get_register_by_value(0)
                self.set_value_to_register(reg['name'], reg['value'], 0)
                self.actualize_register_value(reg['name'], 0)
                return reg
            else:
                address2 = var2['address']
                reg2, reg1, reg3, reg4 = self.get_4_registers(address2)
                self.set_value_to_register(reg1['name'], reg1['value'], var1['value'])
                self.set_value_to_register(reg4['name'], reg4['value'], var1['value'] + 1)
                self.actualize_register_value(reg1['name'], -1)
                self.actualize_register_value(reg4['name'], -1)
                self.actualize_register_value(reg3['name'], -1)
                self.actualize_register_value(reg2['name'], -1)
                self.set_value_to_register(reg3['name'], reg3['value'], 0)
                self.set_value_to_register(reg2['name'], reg2['value'], address2)
                command = {'com': "LOAD", 'arg1': reg2['name'], 'arg2': reg2['name']}
                self.code.append(command)

        elif var1['only_value'] == 0 and var2['only_value'] == 1:
            if var2['value'] == 0:
                reg = self.get_register_by_value(0)
                self.set_value_to_register(reg['name'], reg['value'], 0)
                self.actualize_register_value(reg['name'], 0)
                return reg
            else:
                address1 = var1['address']
                reg1, reg2, reg3, reg4 = self.get_4_registers(address1)
                self.set_value_to_register(reg1['name'], reg1['value'], address1)
                command = {'com': "LOAD", 'arg1': reg1['name'], 'arg2': reg1['name']}
                self.code.append(command)
                self.set_value_to_register(reg2['name'], reg2['value'], var2['value'])
                self.set_value_to_register(reg4['name'], reg4['value'], address1)
                command = {'com': "LOAD", 'arg1': reg4['name'], 'arg2': reg4['name']}
                self.code.append(command)
                command = {'com': "INC", 'arg1': reg4['name'], 'arg2': ""}
                self.code.append(command)
                self.set_value_to_register(reg3['name'], reg3['value'], 0)
                self.actualize_register_value(reg1['name'], -1)
                self.actualize_register_value(reg4['name'], -1)
                self.actualize_register_value(reg3['name'], -1)
                self.actualize_register_value(reg2['name'], -1)


        elif var1['only_value'] == 0 and var2['only_value'] == 0:
            address1 = var1['address']
            address2 = var2['address']
            reg1, reg2, reg3, reg4 = self.get_4_registers(address1)
            self.set_value_to_register(reg1['name'], reg1['value'], address1)
            command = {'com': "LOAD", 'arg1': reg1['name'], 'arg2': reg1['name']}
            self.code.append(command)
            self.set_value_to_register(reg2['name'], reg2['value'], address2)
            command = {'com': "LOAD", 'arg1': reg2['name'], 'arg2': reg2['name']}
            self.code.append(command)
            self.set_value_to_register(reg4['name'], reg4['value'], address1)
            command = {'com': "LOAD", 'arg1': reg4['name'], 'arg2': reg4['name']}
            self.code.append(command)
            command = {'com': "INC", 'arg1': reg4['name'], 'arg2': ""}
            self.code.append(command)
            self.set_value_to_register(reg3['name'], reg3['value'], 0)
            self.actualize_register_value(reg1['name'], -1)
            self.actualize_register_value(reg4['name'], -1)
            self.actualize_register_value(reg3['name'], -1)
            self.actualize_register_value(reg2['name'], -1)

        elif var1['only_value'] == 0 and var2['only_value'] == -2:
            address1 = var1['address']
            reg1, reg2, reg3, reg4 = self.get_4_registers(address1)
            self.set_value_to_register(reg1['name'], reg1['value'], address1)
            command = {'com': "LOAD", 'arg1': reg4['name'], 'arg2': reg1['name']}
            self.code.append(command)
            command = {'com': "INC", 'arg1': reg4['name'], 'arg2': ""}
            self.code.append(command)
            command = {'com': "LOAD", 'arg1': reg1['name'], 'arg2': reg1['name']}
            self.code.append(command)

            self.set_value_to_register(reg2['name'], reg2['value'], var2['address'])
            self.actualize_register_value(reg2['name'], var2['address'])
            self.set_value_to_register(reg3['name'], reg3['value'], var2['name'])
            command = {'com': "LOAD", 'arg1': reg3['name'], 'arg2': reg3['name']}
            self.code.append(command)
            self.actualize_register_value(reg3['name'], -1)
            command = {'com': "ADD", 'arg1': reg2['name'], 'arg2': reg3['name']}
            self.code.append(command)
            command = {'com': "LOAD", 'arg1': reg2['name'], 'arg2': reg2['name']}
            self.code.append(command)
            self.set_value_to_register(reg3['name'], reg3['value'], 0)
            self.actualize_register_value(reg4['name'], -1)

        elif var1['only_value'] == -2 and var2['only_value'] == -2:
            reg1, reg2, reg3, reg4 = self.get_4_registers(var1['address'])
            self.set_value_to_register(reg1['name'], reg1['value'], var1['address'])
            self.actualize_register_value(reg1['name'], -1)
            self.set_value_to_register(reg2['name'], reg2['value'], var1['name'])
            command = {'com': "LOAD", 'arg1': reg2['name'], 'arg2': reg2['name']}
            self.code.append(command)
            self.actualize_register_value(reg2['name'], -1)
            command = {'com': "ADD", 'arg1': reg1['name'], 'arg2': reg2['name']}
            self.code.append(command)
            command = {'com': "LOAD", 'arg1': reg4['name'], 'arg2': reg1['name']}
            self.code.append(command)
            command = {'com': "INC", 'arg1': reg4['name'], 'arg2': ""}
            self.code.append(command)
            command = {'com': "LOAD", 'arg1': reg1['name'], 'arg2': reg1['name']}
            self.code.append(command)

            self.set_value_to_register(reg2['name'], reg2['value'], var2['address'])
            self.actualize_register_value(reg2['name'], var2['address'])
            self.set_value_to_register(reg3['name'], reg3['value'], var2['name'])
            command = {'com': "LOAD", 'arg1': reg3['name'], 'arg2': reg3['name']}
            self.code.append(command)
            self.actualize_register_value(reg3['name'], -1)
            command = {'com': "ADD", 'arg1': reg2['name'], 'arg2': reg3['name']}
            self.code.append(command)
            command = {'com': "LOAD", 'arg1': reg2['name'], 'arg2': reg2['name']}
            self.code.append(command)
            self.set_value_to_register(reg3['name'], reg3['value'], 0)
            self.actualize_register_value(reg4['name'], -1)

        elif var1['only_value'] == -2 and var2['only_value'] == 0:
            reg1, reg2, reg3, reg4 = self.get_4_registers(var1['address'])
            self.set_value_to_register(reg1['name'], reg1['value'], var1['address'])
            self.actualize_register_value(reg1['name'], -1)
            self.set_value_to_register(reg2['name'], reg2['value'], var1['name'])
            command = {'com': "LOAD", 'arg1': reg2['name'], 'arg2': reg2['name']}
            self.code.append(command)
            self.actualize_register_value(reg2['name'], -1)
            command = {'com': "ADD", 'arg1': reg1['name'], 'arg2': reg2['name']}
            self.code.append(command)
            command = {'com': "LOAD", 'arg1': reg4['name'], 'arg2': reg1['name']}
            self.code.append(command)
            command = {'com': "INC", 'arg1': reg4['name'], 'arg2': ""}
            self.code.append(command)
            command = {'com': "LOAD", 'arg1': reg1['name'], 'arg2': reg1['name']}
            self.code.append(command)

            self.set_value_to_register(reg2['name'], reg2['value'], var2['address'])
            command = {'com': "LOAD", 'arg1': reg2['name'], 'arg2': reg2['name']}
            self.code.append(command)
            self.set_value_to_register(reg3['name'], reg3['value'], 0)
            self.actualize_register_value(reg3['name'], -1)
            self.actualize_register_value(reg4['name'], -1)

        elif var1['only_value'] == -2 and var2['only_value'] == 1:
            if var2['value'] == 0:
                reg = self.get_register_by_value(0)
                self.set_value_to_register(reg['name'], reg['value'], 0)
                self.actualize_register_value(reg['name'], 0)
                return reg
            else:
                reg1, reg2, reg3, reg4 = self.get_4_registers(var1['address'])
                self.set_value_to_register(reg1['name'], reg1['value'], var1['address'])
                self.actualize_register_value(reg1['name'], -1)
                self.set_value_to_register(reg2['name'], reg2['value'], var1['name'])
                command = {'com': "LOAD", 'arg1': reg2['name'], 'arg2': reg2['name']}
                self.code.append(command)
                self.actualize_register_value(reg2['name'], -1)
                command = {'com': "ADD", 'arg1': reg1['name'], 'arg2': reg2['name']}
                self.code.append(command)
                command = {'com': "LOAD", 'arg1': reg4['name'], 'arg2': reg1['name']}
                self.code.append(command)
                command = {'com': "INC", 'arg1': reg4['name'], 'arg2': ""}
                self.code.append(command)
                command = {'com': "LOAD", 'arg1': reg1['name'], 'arg2': reg1['name']}
                self.code.append(command)
                self.actualize_register_value(reg4['name'], -1)

                self.set_value_to_register(reg2['name'], reg2['value'], var2['value'])
                self.actualize_register_value(reg2['name'], var2['value'])
                self.actualize_register_value(reg3['name'], -1)
                self.set_value_to_register(reg3['name'], reg3['value'], 0)

        elif var1['only_value'] == 1 and var2['only_value'] == -2:
            if var1['value'] == 0:
                reg = self.get_register_by_value(0)
                self.set_value_to_register(reg['name'], reg['value'], 0)
                self.actualize_register_value(reg['name'], 0)
                return reg
            else:
                reg2, reg1, reg3, reg4 = self.get_4_registers(var2['address'])
                self.set_value_to_register(reg1['name'], reg1['value'], var1['value'])
                self.set_value_to_register(reg4['name'], reg4['value'], var1['value'] + 1)
                self.actualize_register_value(reg1['name'], -1)
                self.actualize_register_value(reg4['name'], -1)
                self.actualize_register_value(reg3['name'], -1)
                self.actualize_register_value(reg2['name'], -1)

                self.set_value_to_register(reg2['name'], reg2['value'], var2['address'])
                self.actualize_register_value(reg2['name'], var2['address'])
                self.set_value_to_register(reg3['name'], reg3['value'], var2['name'])
                command = {'com': "LOAD", 'arg1': reg3['name'], 'arg2': reg3['name']}
                self.code.append(command)
                self.actualize_register_value(reg3['name'], -1)
                command = {'com': "ADD", 'arg1': reg2['name'], 'arg2': reg3['name']}
                self.code.append(command)
                command = {'com': "LOAD", 'arg1': reg2['name'], 'arg2': reg2['name']}
                self.code.append(command)
                self.set_value_to_register(reg3['name'], reg3['value'], 0)
                self.actualize_register_value(reg4['name'], -1)

        command = {'com': "JZERO", 'arg1': reg2['name'], 'arg2': str(8)}
        self.code.append(command)
        command = {'com': "SUB", 'arg1': reg1['name'], 'arg2': reg2['name']}
        self.code.append(command)
        command = {'com': "SUB", 'arg1': reg4['name'], 'arg2': reg2['name']}
        self.code.append(command)
        command = {'com': "JZERO", 'arg1': reg1['name'], 'arg2': str(3)}
        self.code.append(command)
        command = {'com': "INC", 'arg1': reg3['name'], 'arg2': ""}
        self.code.append(command)
        command = {'com': "JUMP", 'arg1': str(-4), 'arg2': ""}
        self.code.append(command)
        command = {'com': "JZERO", 'arg1': reg4['name'], 'arg2': str(2)}
        self.code.append(command)
        command = {'com': "INC", 'arg1': reg3['name'], 'arg2': ""}
        self.code.append(command)
        return reg3

    def expression_modulo(self, var1, var2):
        if isinstance(var1, list):
            var1 = var1[0]
        if isinstance(var2, list):
            var2 = var2[0]
        if var1['value'] == -1 and var1['table'] == 0 and var1['iterator'] == 0:
            print("Zmienna ", var1['name'], " nie zainicjalizowana")
            sys.exit()
        elif var2['value'] == -1 and var2['table'] == 0 and var2['iterator'] == 0:
            print("Zmienna ", var2['name'], " nie zainicjalizowana")
            sys.exit()

        if var1['only_value'] == 1 and var2['only_value'] == 1:
            if var2['value'] == 0:
                result = 0
            else:
                result = var1['value'] % var2['value']
            reg = self.get_register_by_value(result)
            self.set_value_to_register(reg['name'], reg['value'], result)
            self.actualize_register_value(reg['name'], result)
            return reg
        elif var1['only_value'] == 1 and var2['only_value'] == 0:
            if var1['value'] == 0:
                reg = self.get_register_by_value(0)
                self.set_value_to_register(reg['name'], reg['value'], 0)
                self.actualize_register_value(reg['name'], 0)
                return reg
            else:
                address2 = var2['address']
                reg2, reg1, reg4 = self.get_3_registers(address2)
                self.set_value_to_register(reg1['name'], reg1['value'], var1['value'])
                self.set_value_to_register(reg4['name'], reg4['value'], var1['value'] + 1)
                self.actualize_register_value(reg1['name'], -1)
                self.actualize_register_value(reg4['name'], -1)
                self.actualize_register_value(reg2['name'], -1)
                self.set_value_to_register(reg2['name'], reg2['value'], address2)
                command = {'com': "LOAD", 'arg1': reg2['name'], 'arg2': reg2['name']}
                self.code.append(command)

        elif var1['only_value'] == 0 and var2['only_value'] == 1:
            if var2['value'] == 0:
                reg = self.get_register_by_value(0)
                self.set_value_to_register(reg['name'], reg['value'], 0)
                self.actualize_register_value(reg['name'], 0)
                return reg
            else:
                address1 = var1['address']
                reg1, reg2, reg4 = self.get_3_registers(address1)
                self.set_value_to_register(reg1['name'], reg1['value'], address1)
                command = {'com': "LOAD", 'arg1': reg1['name'], 'arg2': reg1['name']}
                self.code.append(command)
                self.set_value_to_register(reg2['name'], reg2['value'], var2['value'])
                self.set_value_to_register(reg4['name'], reg4['value'], address1)
                command = {'com': "LOAD", 'arg1': reg4['name'], 'arg2': reg4['name']}
                self.code.append(command)
                command = {'com': "INC", 'arg1': reg4['name'], 'arg2': ""}
                self.code.append(command)
                self.actualize_register_value(reg1['name'], -1)
                self.actualize_register_value(reg4['name'], -1)
                self.actualize_register_value(reg2['name'], -1)

        elif var1['only_value'] == 0 and var2['only_value'] == 0:
            address1 = var1['address']
            address2 = var2['address']
            reg1, reg2, reg4 = self.get_3_registers(address1)
            self.set_value_to_register(reg1['name'], reg1['value'], address1)
            command = {'com': "LOAD", 'arg1': reg1['name'], 'arg2': reg1['name']}
            self.code.append(command)
            self.set_value_to_register(reg2['name'], reg2['value'], address2)
            command = {'com': "LOAD", 'arg1': reg2['name'], 'arg2': reg2['name']}
            self.code.append(command)
            self.set_value_to_register(reg4['name'], reg4['value'], address1)
            command = {'com': "LOAD", 'arg1': reg4['name'], 'arg2': reg4['name']}
            self.code.append(command)
            command = {'com': "INC", 'arg1': reg4['name'], 'arg2': ""}
            self.code.append(command)
            self.actualize_register_value(reg1['name'], -1)
            self.actualize_register_value(reg4['name'], -1)
            self.actualize_register_value(reg2['name'], -1)

        elif var1['only_value'] == -2 and var2['only_value'] == -2:
            reg1, reg2, reg3, reg4 = self.get_4_registers(var1['address'])
            self.set_value_to_register(reg1['name'], reg1['value'], var1['address'])
            self.actualize_register_value(reg1['name'], -1)
            self.set_value_to_register(reg2['name'], reg2['value'], var1['name'])
            command = {'com': "LOAD", 'arg1': reg2['name'], 'arg2': reg2['name']}
            self.code.append(command)
            self.actualize_register_value(reg2['name'], -1)
            command = {'com': "ADD", 'arg1': reg1['name'], 'arg2': reg2['name']}
            self.code.append(command)
            command = {'com': "LOAD", 'arg1': reg4['name'], 'arg2': reg1['name']}
            self.code.append(command)
            command = {'com': "INC", 'arg1': reg4['name'], 'arg2': ""}
            self.code.append(command)
            command = {'com': "LOAD", 'arg1': reg1['name'], 'arg2': reg1['name']}
            self.code.append(command)

            self.set_value_to_register(reg2['name'], reg2['value'], var2['address'])
            self.actualize_register_value(reg2['name'], var2['address'])
            self.set_value_to_register(reg3['name'], reg3['value'], var2['name'])
            command = {'com': "LOAD", 'arg1': reg3['name'], 'arg2': reg3['name']}
            self.code.append(command)
            self.actualize_register_value(reg3['name'], -1)
            command = {'com': "ADD", 'arg1': reg2['name'], 'arg2': reg3['name']}
            self.code.append(command)
            command = {'com': "LOAD", 'arg1': reg2['name'], 'arg2': reg2['name']}
            self.code.append(command)
            self.actualize_register_value(reg4['name'], -1)

        elif var1['only_value'] == 1 and var2['only_value'] == -2:
            if var1['value'] == 0:
                reg = self.get_register_by_value(0)
                self.set_value_to_register(reg['name'], reg['value'], 0)
                self.actualize_register_value(reg['name'], 0)
                return reg
            else:
                reg2, reg1, reg3, reg4 = self.get_4_registers(var2['address'])
                self.set_value_to_register(reg1['name'], reg1['value'], var1['value'])
                self.set_value_to_register(reg4['name'], reg4['value'], var1['value'] + 1)
                self.actualize_register_value(reg1['name'], -1)
                self.actualize_register_value(reg4['name'], -1)
                self.actualize_register_value(reg3['name'], -1)
                self.actualize_register_value(reg2['name'], -1)

                self.set_value_to_register(reg2['name'], reg2['value'], var2['address'])
                self.actualize_register_value(reg2['name'], var2['address'])
                command = {'com': "LOAD", 'arg1': reg3['name'], 'arg2': reg3['name']}
                self.code.append(command)
                self.actualize_register_value(reg3['name'], -1)
                command = {'com': "ADD", 'arg1': reg2['name'], 'arg2': reg3['name']}
                self.code.append(command)
                command = {'com': "LOAD", 'arg1': reg2['name'], 'arg2': reg2['name']}
                self.code.append(command)

        elif var1['only_value'] == -2 and var2['only_value'] == 1:
            if var2['value'] == 0:
                reg = self.get_register_by_value(0)
                self.set_value_to_register(reg['name'], reg['value'], 0)
                self.actualize_register_value(reg['name'], 0)
                return reg
            else:
                reg1, reg2, reg3, reg4 = self.get_4_registers(var1['address'])
                self.set_value_to_register(reg1['name'], reg1['value'], var1['address'])
                self.actualize_register_value(reg1['name'], -1)
                self.set_value_to_register(reg2['name'], reg2['value'], var1['name'])
                command = {'com': "LOAD", 'arg1': reg2['name'], 'arg2': reg2['name']}
                self.code.append(command)
                self.actualize_register_value(reg2['name'], -1)
                command = {'com': "ADD", 'arg1': reg1['name'], 'arg2': reg2['name']}
                self.code.append(command)
                command = {'com': "LOAD", 'arg1': reg4['name'], 'arg2': reg1['name']}
                self.code.append(command)
                command = {'com': "INC", 'arg1': reg4['name'], 'arg2': ""}
                self.code.append(command)
                command = {'com': "LOAD", 'arg1': reg1['name'], 'arg2': reg1['name']}
                self.code.append(command)
                self.actualize_register_value(reg4['name'], -1)

                self.set_value_to_register(reg2['name'], reg2['value'], var2['value'])
                self.actualize_register_value(reg2['name'], var2['value'])
                self.actualize_register_value(reg3['name'], -1)

        elif var1['only_value'] == -2 and var2['only_value'] == 0:
            reg1, reg2, reg3, reg4 = self.get_4_registers(var1['address'])
            self.set_value_to_register(reg1['name'], reg1['value'], var1['address'])
            self.actualize_register_value(reg1['name'], -1)
            self.set_value_to_register(reg2['name'], reg2['value'], var1['name'])
            command = {'com': "LOAD", 'arg1': reg2['name'], 'arg2': reg2['name']}
            self.code.append(command)
            self.actualize_register_value(reg2['name'], -1)
            command = {'com': "ADD", 'arg1': reg1['name'], 'arg2': reg2['name']}
            self.code.append(command)
            command = {'com': "LOAD", 'arg1': reg4['name'], 'arg2': reg1['name']}
            self.code.append(command)
            command = {'com': "INC", 'arg1': reg4['name'], 'arg2': ""}
            self.code.append(command)
            command = {'com': "LOAD", 'arg1': reg1['name'], 'arg2': reg1['name']}
            self.code.append(command)

            self.set_value_to_register(reg2['name'], reg2['value'], var2['address'])
            command = {'com': "LOAD", 'arg1': reg2['name'], 'arg2': reg2['name']}
            self.code.append(command)
            self.actualize_register_value(reg3['name'], -1)
            self.actualize_register_value(reg4['name'], -1)

        elif var1['only_value'] == 0 and var2['only_value'] == -2:
            address1 = var1['address']
            reg1, reg2, reg3, reg4 = self.get_4_registers(address1)
            self.set_value_to_register(reg1['name'], reg1['value'], address1)
            command = {'com': "LOAD", 'arg1': reg4['name'], 'arg2': reg1['name']}
            self.code.append(command)
            command = {'com': "INC", 'arg1': reg4['name'], 'arg2': ""}
            self.code.append(command)
            command = {'com': "LOAD", 'arg1': reg1['name'], 'arg2': reg1['name']}
            self.code.append(command)

            self.set_value_to_register(reg2['name'], reg2['value'], var2['address'])
            self.actualize_register_value(reg2['name'], var2['address'])
            self.set_value_to_register(reg3['name'], reg3['value'], var2['name'])
            command = {'com': "LOAD", 'arg1': reg3['name'], 'arg2': reg3['name']}
            self.code.append(command)
            self.actualize_register_value(reg3['name'], -1)
            command = {'com': "ADD", 'arg1': reg2['name'], 'arg2': reg3['name']}
            self.code.append(command)
            command = {'com': "LOAD", 'arg1': reg2['name'], 'arg2': reg2['name']}
            self.code.append(command)
            self.actualize_register_value(reg4['name'], -1)

        command = {'com': "JZERO", 'arg1': reg2['name'], 'arg2': str(2)}
        self.code.append(command)
        command = {'com': "JUMP", 'arg1': str(3), 'arg2': ""}
        self.code.append(command)
        command = {'com': "RESET", 'arg1': reg1['name'], 'arg2': ""}
        self.code.append(command)
        command = {'com': "JUMP", 'arg1': str(5), 'arg2': ""}
        self.code.append(command)
        command = {'com': "SUB", 'arg1': reg4['name'], 'arg2': reg2['name']}
        self.code.append(command)
        command = {'com': "JZERO", 'arg1': reg4['name'], 'arg2': str(3)}
        self.code.append(command)
        command = {'com': "SUB", 'arg1': reg1['name'], 'arg2': reg2['name']}
        self.code.append(command)
        command = {'com': "JUMP", 'arg1': str(-3), 'arg2': ""}
        self.code.append(command)
        return reg1

    def assign(self, reg, var, iterator=0):
        if isinstance(var, list):
            var = var[0]
        if isinstance(reg, list):
            reg = reg[0]
        if iterator == 0 and var['iterator'] == 1:
            print("Modyfikacja iteratora")
            sys.exit()
        if var['value'] == -2:
            reg1, reg2 = self.get_2_registers_diff(reg['name'])
            if var['address'] == -1:
                self.set_value_to_register(reg2['name'], reg2['value'], int(var['name']))
                command = {'com': "LOAD", 'arg1': reg2['name'], 'arg2': reg2['name']}
                self.code.append(command)
                self.actualize_register_value(reg2['name'], -1)
                command = {'com': "DEC", 'arg1': reg2['name'], 'arg2': ""}
                self.code.append(command)
                command = {'com': "STORE", 'arg1': reg['name'], 'arg2': reg2['name']}
                self.code.append(command)
            elif var['address'] < 0:
                self.set_value_to_register(reg1['name'], reg1['value'], var['name'])
                command = {'com': "LOAD", 'arg1': reg1['name'], 'arg2': reg1['name']}
                self.code.append(command)
                self.set_value_to_register(reg2['name'], reg2['value'], abs(int(var['address'])))
                command = {'com': "SUB", 'arg1': reg1['name'], 'arg2': reg2['name']}
                self.code.append(command)
                command = {'com': "STORE", 'arg1': reg['name'], 'arg2': reg1['name']}
                self.code.append(command)
                self.actualize_register_value(reg1['name'], -1)
                self.actualize_register_value(reg2['name'], abs(int(var['address'])))
            else:
                self.set_value_to_register(reg1['name'], reg1['value'], var['address'])
                self.actualize_register_value(reg1['name'], var['address'])
                self.set_value_to_register(reg2['name'], reg2['value'], int(var['name']))
                command = {'com': "LOAD", 'arg1': reg2['name'], 'arg2': reg2['name']}
                self.code.append(command)
                self.actualize_register_value(reg2['name'], -1)
                command = {'com': "ADD", 'arg1': reg1['name'], 'arg2': reg2['name']}
                self.code.append(command)
                command = {'com': "STORE", 'arg1': reg['name'], 'arg2': reg1['name']}
                self.code.append(command)

        else:
            address = var['address']
            address_reg = self.get_register_diff(reg['name'])
            self.set_value_to_register(address_reg['name'], address_reg['value'], address)
            self.actualize_register_value(address_reg['name'], address)
            self.actualize_register_value(reg['name'], -1)
            command = {'com': "STORE", 'arg1': reg['name'], 'arg2': address_reg['name']}
            self.code.append(command)

    def condition_1(self, var1, var2, sign):
        if isinstance(var1, list):
            var1 = var1[0]
        if isinstance(var2, list):
            var2 = var2[0]

        start = len(self.code)
        result = 0
        jump = []
        if var1['only_value'] == 1 and var2['only_value'] == 1:
            if (var1['value'] == var2['value']) and (sign == '=' or sign == '>=' or sign == '<='):
                result = 1
            elif (var1['value'] == var2['value']) and (sign == '!=' or sign == '>' or sign == '<'):
                result = 0
            elif (var1['value'] > var2['value']) and (sign == '!=' or sign == '>=' or sign == '>'):
                result = 1
            elif (var1['value'] > var2['value']) and (sign == '=' or sign == '<=' or sign == '<'):
                result = 0
            elif (var1['value'] < var2['value']) and (sign == '!=' or sign == '<=' or sign == '<'):
                result = 1
            elif (var1['value'] < var2['value']) and (sign == '=' or sign == '>=' or sign == '>'):
                result = 0

            if result == 1:
                jump = -1  # nie pisac jumpa bo warunek zawsze prawdziwy
            else:
                command = {'com': "JUMP", 'arg1': "", 'arg2': ""}
                self.code.append(command)
                jump = len(self.code) - 1

            return start, jump

        elif var1['only_value'] == 1 and var2['only_value'] == 0:
            address2 = var2['address']
            reg1 = self.r5
            reg2 = self.r6
            self.set_value_to_register(reg1['name'], -1, var1['value'])
            self.set_value_to_register(reg2['name'], -1, address2)
            self.actualize_register_value(reg1['name'], -1)
            self.actualize_register_value(reg2['name'], -1)
            command = {'com': "LOAD", 'arg1': reg2['name'], 'arg2': reg2['name']}
            self.code.append(command)

        elif var1['only_value'] == 0 and var2['only_value'] == 1:
            address1 = var1['address']
            reg1 = self.r5
            reg2 = self.r6
            self.set_value_to_register(reg1['name'], -1, address1)
            self.set_value_to_register(reg2['name'], -1, var2['value'])
            self.actualize_register_value(reg1['name'], -1)
            self.actualize_register_value(reg2['name'], -1)
            command = {'com': "LOAD", 'arg1': reg1['name'], 'arg2': reg1['name']}
            self.code.append(command)

        elif var1['only_value'] == 0 and var2['only_value'] == 0:
            address1 = var1['address']
            address2 = var2['address']
            reg1 = self.r5
            reg2 = self.r6
            self.set_value_to_register(reg1['name'], -1, address1)
            command = {'com': "LOAD", 'arg1': reg1['name'], 'arg2': reg1['name']}
            self.code.append(command)
            self.set_value_to_register(reg2['name'], -1, address2)
            self.actualize_register_value(reg1['name'], -1)
            self.actualize_register_value(reg2['name'], -1)
            command = {'com': "LOAD", 'arg1': reg2['name'], 'arg2': reg2['name']}
            self.code.append(command)

        elif var1['only_value'] == -2 and var2['only_value'] == -2:
            reg1, reg2, reg3 = self.r5, self.r6, self.r4
            self.set_value_to_register(reg1['name'], reg1['value'], var1['address'])
            self.actualize_register_value(reg1['name'], -1)
            self.set_value_to_register(reg2['name'], reg2['value'], var1['name'])
            command = {'com': "LOAD", 'arg1': reg2['name'], 'arg2': reg2['name']}
            self.code.append(command)
            self.actualize_register_value(reg2['name'], -1)
            command = {'com': "ADD", 'arg1': reg1['name'], 'arg2': reg2['name']}
            self.code.append(command)
            command = {'com': "LOAD", 'arg1': reg1['name'], 'arg2': reg1['name']}
            self.code.append(command)

            self.set_value_to_register(reg2['name'], reg2['value'], var2['address'])
            self.actualize_register_value(reg2['name'], var2['address'])
            self.set_value_to_register(reg3['name'], reg3['value'], var2['name'])
            command = {'com': "LOAD", 'arg1': reg3['name'], 'arg2': reg3['name']}
            self.code.append(command)
            self.actualize_register_value(reg3['name'], -1)
            command = {'com': "ADD", 'arg1': reg2['name'], 'arg2': reg3['name']}
            self.code.append(command)
            command = {'com': "LOAD", 'arg1': reg2['name'], 'arg2': reg2['name']}
            self.code.append(command)

        elif var1['only_value'] == -2 and var2['only_value'] == 1:
            reg1, reg2 = self.r5, self.r6
            self.set_value_to_register(reg1['name'], reg1['value'], var1['address'])
            self.actualize_register_value(reg1['name'], -1)
            self.set_value_to_register(reg2['name'], reg2['value'], var1['name'])
            command = {'com': "LOAD", 'arg1': reg2['name'], 'arg2': reg2['name']}
            self.code.append(command)
            self.actualize_register_value(reg2['name'], -1)
            command = {'com': "ADD", 'arg1': reg1['name'], 'arg2': reg2['name']}
            self.code.append(command)
            command = {'com': "LOAD", 'arg1': reg1['name'], 'arg2': reg1['name']}
            self.code.append(command)

            self.set_value_to_register(reg2['name'], -1, var2['value'])
            self.actualize_register_value(reg2['name'], -1)

        elif var1['only_value'] == 1 and var2['only_value'] == -2:
            reg1, reg2 = self.r5, self.r6
            self.set_value_to_register(reg2['name'], reg2['value'], var2['address'])
            self.actualize_register_value(reg2['name'], -1)
            self.set_value_to_register(reg1['name'], reg1['value'], var2['name'])
            command = {'com': "LOAD", 'arg1': reg1['name'], 'arg2': reg1['name']}
            self.code.append(command)
            self.actualize_register_value(reg1['name'], -1)
            command = {'com': "ADD", 'arg1': reg2['name'], 'arg2': reg1['name']}
            self.code.append(command)
            command = {'com': "LOAD", 'arg1': reg2['name'], 'arg2': reg2['name']}
            self.code.append(command)

            self.set_value_to_register(reg1['name'], -1, var1['value'])
            self.actualize_register_value(reg1['name'], -1)

        elif var1['only_value'] == -2 and var2['only_value'] == 0:
            reg1, reg2 = self.r5, self.r6
            if var1['address'] == -1:
                self.set_value_to_register(reg1['name'], reg1['value'], var1['name'])
                self.actualize_register_value(reg2['name'], -1)
                command = {'com': "LOAD", 'arg1': reg1['name'], 'arg2': reg1['name']}
                self.code.append(command)
                command = {'com': "DEC", 'arg1': reg1['name'], 'arg2': ""}
                self.code.append(command)
                command = {'com': "LOAD", 'arg1': reg1['name'], 'arg2': reg1['name']}
                self.code.append(command)
            else:
                self.set_value_to_register(reg1['name'], reg1['value'], var1['address'])
                self.actualize_register_value(reg1['name'], -1)
                self.set_value_to_register(reg2['name'], reg2['value'], var1['name'])
                command = {'com': "LOAD", 'arg1': reg2['name'], 'arg2': reg2['name']}
                self.code.append(command)
                self.actualize_register_value(reg2['name'], -1)
                command = {'com': "ADD", 'arg1': reg1['name'], 'arg2': reg2['name']}
                self.code.append(command)
                command = {'com': "LOAD", 'arg1': reg1['name'], 'arg2': reg1['name']}
                self.code.append(command)

            self.set_value_to_register(reg2['name'], -1, var2['address'])
            self.actualize_register_value(reg2['name'], -1)
            command = {'com': "LOAD", 'arg1': reg2['name'], 'arg2': reg2['name']}
            self.code.append(command)

        elif var1['only_value'] == 0 and var2['only_value'] == -2:
            print("Condition: ", var1, var2)
            reg1, reg2 = self.r5, self.r6
            """
            self.set_value_to_register(reg2['name'], reg2['value'], var2['address'])
            self.actualize_register_value(reg2['name'], -1)
            self.set_value_to_register(reg1['name'], reg1['value'], var2['name'])
            command = {'com': "LOAD", 'arg1': reg1['name'], 'arg2': reg1['name']}
            self.code.append(command)
            self.actualize_register_value(reg1['name'], -1)
            command = {'com': "ADD", 'arg1': reg2['name'], 'arg2': reg1['name']}
            self.code.append(command)
            command = {'com': "LOAD", 'arg1': reg2['name'], 'arg2': reg2['name']}
            self.code.append(command)
            """
            self.set_value_to_register(reg1['name'], -1, var1['address'])
            command = {'com': "LOAD", 'arg1': reg1['name'], 'arg2': reg1['name']}
            self.code.append(command)
            self.set_value_to_register(reg2['name'], -1, var2['address'])
            self.actualize_register_value(reg1['name'], -1)
            self.actualize_register_value(reg2['name'], -1)
            command = {'com': "LOAD", 'arg1': reg2['name'], 'arg2': reg2['name']}
            self.code.append(command)


        if sign == '>':
            command = {'com': "SUB", 'arg1': reg1['name'], 'arg2': reg2['name']}
            self.code.append(command)
            command = {'com': "JZERO", 'arg1': reg1['name'], 'arg2': ""}
            self.code.append(command)
        elif sign == '<':
            command = {'com': "SUB", 'arg1': reg2['name'], 'arg2': reg1['name']}
            self.code.append(command)
            command = {'com': "JZERO", 'arg1': reg2['name'], 'arg2': ""}
            self.code.append(command)
        elif sign == '>=':
            command = {'com': "INC", 'arg1': reg1['name'], 'arg2': ""}
            self.code.append(command)
            command = {'com': "SUB", 'arg1': reg1['name'], 'arg2': reg2['name']}
            self.code.append(command)
            command = {'com': "JZERO", 'arg1': reg1['name'], 'arg2': ""}
            self.code.append(command)
        elif sign == '<=':
            command = {'com': "INC", 'arg1': reg2['name'], 'arg2': ""}
            self.code.append(command)
            command = {'com': "SUB", 'arg1': reg2['name'], 'arg2': reg1['name']}
            self.code.append(command)
            command = {'com': "JZERO", 'arg1': reg2['name'], 'arg2': ""}
            self.code.append(command)
        elif sign == '=' or sign == '!=':
            reg3 = self.r4
            command = {'com': "RESET", 'arg1': reg3['name'], 'arg2': ""}
            self.code.append(command)
            command = {'com': "ADD", 'arg1': reg3['name'], 'arg2': reg1['name']}
            self.code.append(command)
            command = {'com': "SUB", 'arg1': reg1['name'], 'arg2': reg2['name']}
            self.code.append(command)
            command = {'com': "SUB", 'arg1': reg2['name'], 'arg2': reg3['name']}
            self.code.append(command)

            if sign == '=':
                command = {'com': "JZERO", 'arg1': reg1['name'], 'arg2': str(2)}
                self.code.append(command)
                command = {'com': "JUMP", 'arg1': "", 'arg2': ""}
                self.code.append(command)
                jump.append(len(self.code) - 1)
                command = {'com': "JZERO", 'arg1': reg2['name'], 'arg2': str(2)}
                self.code.append(command)
                command = {'com': "JUMP", 'arg1': "", 'arg2': ""}
                self.code.append(command)
            elif sign == '!=':
                command = {'com': "JZERO", 'arg1': reg1['name'], 'arg2': str(2)}
                self.code.append(command)
                command = {'com': "JUMP", 'arg1': str(2), 'arg2': ""}
                self.code.append(command)
                command = {'com': "JZERO", 'arg1': reg2['name'], 'arg2': ""}
                self.code.append(command)

        jump.append(len(self.code) - 1)
        return start, jump

    def just_if(self, jump, length):
        if len(jump) == 1:
            how_many_skip = length - jump[0]
            j = self.code[jump[0]]
            j['arg2'] = how_many_skip
            self.code[jump[0]] = j
        else:
            how_many_skip = length - jump[0]
            j = self.code[jump[0]]
            j['arg1'] = how_many_skip
            self.code[jump[0]] = j
            j = self.code[jump[1]]
            j['arg1'] = how_many_skip - 2
            self.code[jump[1]] = j

    def if_else(self, jump, then_l, else_l):
        if len(jump) == 1:
            how_many_skip = then_l + 1
            j = self.code[jump[0]]
            j['arg2'] = how_many_skip + 1
            self.code[jump[0]] = j

        else:
            how_many_skip = then_l + 1 + 2
            j = self.code[jump[0]]
            j['arg1'] = how_many_skip + 1
            self.code[jump[0]] = j
            how_many_skip -= 2
            j = self.code[jump[1]]
            j['arg1'] = how_many_skip + 1
            self.code[jump[1]] = j

        command = {'com': "JUMP", 'arg1': str(else_l + 1), 'arg2': ""}
        self.code.insert(jump[0] + then_l + 1, command)

    def while_command(self, length, jump, start):
        if len(jump) == 1:
            how_many_skip = length - jump[0] + 1
            j = self.code[jump[0]]
            j['arg2'] = how_many_skip
            self.code[jump[0]] = j
        else:
            how_many_skip = length - jump[1] + 1
            j = self.code[jump[1]]
            j['arg1'] = how_many_skip
            self.code[jump[1]] = j
            how_many_skip += 2
            j = self.code[jump[0]]
            j['arg1'] = how_many_skip
            self.code[jump[0]] = j

        back = length - start
        command = {'com': "JUMP", 'arg1': str(-back), 'arg2': ""}
        self.code.append(command)

    def repeat_until(self, length, jump):
        if len(jump) == 1:
            j = self.code[jump[0]]
            j['arg2'] = 2
            self.code[jump[0]] = j
        else:
            j = self.code[jump[1]]
            j['arg1'] = 2
            self.code[jump[1]] = j
            j = self.code[jump[0]]
            j['arg1'] = 4
            self.code[jump[0]] = j

        command = {'com': "JUMP", 'arg1': str(-length), 'arg2': ""}
        self.code.append(command)

    def delete_alt_orders(self, how_many):
        for i in range(how_many):
            self.code.pop()

    def copy_code(self, start):
        new_list = self.code[start:]
        self.delete_alt_orders(len(self.code) - start)
        return new_list

    def insert_into_code(self, to_insert, start):
        c = 0
        jump=-1
        for i in to_insert:
            if i['com'] == 'JZERO':
                jump = start+c
            self.code.insert(start+c, i)
            c += 1
        return jump

    def for_jump(self, jump, how_many):
        j = self.code[jump[0]]
        j['arg2'] = how_many
        self.code[jump[0]] = j

    def for_dec_iterator(self, iterator, sign):
        if isinstance(iterator, list):
            iterator = iterator[0]
        address = iterator['address']
        reg, reg2 = self.get_2_registers(address)
        self.set_value_to_register(reg['name'], reg['value'], address)
        command = {'com': "LOAD", 'arg1': reg2['name'], 'arg2': reg['name']}
        self.code.append(command)
        if sign == '-':
            command = {'com': "JZERO", 'arg1': reg2['name'], 'arg2': str(4)}
            self.code.append(command)
            command = {'com': "DEC", 'arg1': reg2['name'], 'arg2': ""}
        elif sign == '+':
            command = {'com': "INC", 'arg1': reg2['name'], 'arg2': ""}
        self.code.append(command)
        command = {'com': "STORE", 'arg1': reg2['name'], 'arg2': reg['name']}
        self.code.append(command)

    def for_jump2(self, jump, how_many_add):
        j = self.code[jump]
        j['arg2'] = int(j['arg2']) + how_many_add
        self.code[jump] = j

    def add_jump_to_for(self, how_many_jump):
        command = {'com': "JUMP", 'arg1': str(-how_many_jump), 'arg2': ""}
        self.code.append(command)

    def load_to_memory(self, var1, var2):
        if isinstance(var1, list):
            var1 = var1[0]
        if isinstance(var2, list):
            var2 = var2[0]
        add_from = var1['address']
        add_to = var2['address']
        reg1, reg2 = self.get_2_registers(add_to)

        if var1['only_value'] == -2:
            if add_from < 0:
                print(var1, var2)
                self.set_value_to_register(reg1['name'], reg1['value'], var1['name'])
                command = {'com': "LOAD", 'arg1': reg1['name'], 'arg2': reg1['name']}
                self.code.append(command)
                self.set_value_to_register(reg2['name'], reg2['value'], abs(int(var1['address'])))
                command = {'com': "SUB", 'arg1': reg1['name'], 'arg2': reg2['name']}
                self.code.append(command)
                command = {'com': "LOAD", 'arg1': reg1['name'], 'arg2': reg1['name']}
                self.code.append(command)
                self.actualize_register_value(reg1['name'], -1)
                self.actualize_register_value(reg2['name'], abs(int(var1['address'])))

            else:
                self.set_value_to_register(reg1['name'], reg1['value'], add_from)
                self.actualize_register_value(reg1['name'], add_from)
                self.set_value_to_register(reg2['name'], reg2['value'], var1['name'])
                command = {'com': "LOAD", 'arg1': reg2['name'], 'arg2': reg2['name']}
                self.code.append(command)
                self.actualize_register_value(reg2['name'], -1)
                command = {'com': "ADD", 'arg1': reg1['name'], 'arg2': reg2['name']}
                self.code.append(command)
                command = {'com': "LOAD", 'arg1': reg1['name'], 'arg2': reg1['name']}
                self.code.append(command)
        elif var1['only_value'] == 0:
            self.set_value_to_register(reg1['name'], reg1['value'], add_from)
            command = {'com': "LOAD", 'arg1': reg1['name'], 'arg2': reg1['name']}
            self.code.append(command)
            self.actualize_register_value(reg1['name'], -1)
        elif var1['only_value'] == 1:
            self.set_value_to_register(reg1['name'], reg1['value'], var1['value'])

        self.set_value_to_register(reg2['name'], reg2['value'], add_to)
        command = {'com': "STORE", 'arg1': reg1['name'], 'arg2': reg2['name']}
        self.code.append(command)
