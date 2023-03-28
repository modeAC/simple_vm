from processor import VMProcessor

if __name__ == '__main__':
    bytecode = [0x00,
                0x01, 0x00, 0x03,
                0x02, 0x00,
                0x01, 0x01, 0x02,
                0x03, 0x00, 0x01]

    vm = VMProcessor()
    vm.run(bytecode)
