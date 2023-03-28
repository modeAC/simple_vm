from typing import List, Optional


class VMProcessor:
    iter: Optional[int] = None
    reg: List[int] = [0] * 16

    def __init__(self):
        """
        bytecode


        0x00 idle:  1 byte, no ops - idle command
        0x01 load:  3 byte, 2 op   - load op1 to reg[op0]
        0x02 inc:   2 byte, 1 op   - inc reg[op]
        0x03 add:   3 byte, 2 ops  - reg[op0] = reg[op0] + reg[op1]
        """

        self.cmds = {
            0x00: self.__idle,
            0x01: self.__load,
            0x02: self.__inc,
            0x03: self.__add
        }

    def run(self, bytecode: list, start_iter: int = 0):
        self.iter = start_iter

        while self.iter < len(bytecode):
            try:
                op = bytecode[self.iter]
            except KeyError as e:
                raise ValueError('unknown command')

            self.cmds[op](bytecode)
            self.iter += 1

        self.iter = None

    def reset(self):
        self.reg = [0] * 16
        self.iter = None

    def __idle(self, bytecode):
        print('idle')
        pass

    def __load(self, bytecode):
        try:
            op0 = self.__next_op(bytecode)
            op1 = self.__next_op(bytecode)
            self.reg[op0] = op1
            print(f'reg[{op0}]: {self.reg[op0]}')
        except IndexError as e:
            raise ValueError

    def __inc(self, bytecode):
        try:
            op0 = self.__next_op(bytecode)
            self.reg[op0] += 1
            print(f'reg[{op0}]: {self.reg[op0]}')
        except IndexError as e:
            raise ValueError

    def __add(self, bytecode):
        try:
            op0 = self.__next_op(bytecode)
            op1 = self.__next_op(bytecode)
            self.reg[op0] = self.reg[op0] + self.reg[op1]
            print(f'reg[{op0}]: {self.reg[op0]}')
        except IndexError as e:
            raise ValueError

    def __next_op(self, bytecode):
        self.iter += 1
        return bytecode[self.iter]
