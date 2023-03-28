from typing import List, Optional


class VMProcessor:
    iter: Optional[int] = None
    reg: List[int] = [None] * 16

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

    def run(self, bytecode: list):
        self.iter = 0

        while self.iter < len(bytecode):
            op = bytecode[self.iter]
            self.cmds[op](bytecode)
            self.iter += 1

    def __idle(self, bytecode):
        print('idle')
        pass

    def __load(self, bytecode):
        op0 = self.__next_op(bytecode)
        op1 = self.__next_op(bytecode)
        self.reg[op0] = op1
        print(f'reg[{op0}]: {self.reg[op0]}')

    def __inc(self, bytecode):
        op0 = self.__next_op(bytecode)
        self.reg[op0] += 1
        print(f'reg[{op0}]: {self.reg[op0]}')

    def __add(self, bytecode):
        op0 = self.__next_op(bytecode)
        op1 = self.__next_op(bytecode)
        self.reg[op0] = self.reg[op0] + self.reg[op1]
        print(f'reg[{op0}]: {self.reg[op0]}')

    def __next_op(self, bytecode):
        self.iter += 1
        return bytecode[self.iter]


if __name__ == '__main__':
    vm = VMProcessor()

    vm.run([0x00])
    