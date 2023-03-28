import unittest

from processor import VMProcessor


class TestProcessor(unittest.TestCase):
    vm = VMProcessor()

    def setUp(self) -> None:
        self.vm.reset()

    def test_load(self):
        bytecode = [0x01, 0x00, 0x03]
        self.vm.run(bytecode)
        self.assertEqual(0x03, self.vm.reg[0x00])

    def test_load_raise(self):
        with self.assertRaises(ValueError):
            bytecode = [0x01, 0x17, 0x03]
            self.vm.run(bytecode)

    def test_inc(self):
        bytecode = [0x02, 0x00]
        self.vm.run(bytecode)
        self.assertEqual(0x01, self.vm.reg[0x00])

    def test_inc_raise(self):
        with self.assertRaises(ValueError):
            bytecode = [0x02, 0x17]
            self.vm.run(bytecode)

    def test_add(self):
        bytecode = [0x01, 0x00, 0x03]
        self.vm.run(bytecode)
        bytecode = [0x01, 0x01, 0x03]
        self.vm.run(bytecode)

        bytecode = [0x03, 0x00, 0x01]
        self.vm.run(bytecode)
        self.assertEqual(0x06, self.vm.reg[0x00])

    def test_add_raise(self):
        with self.assertRaises(ValueError):
            bytecode = [0x01, 0x00, 0x03]
            self.vm.run(bytecode)
            bytecode = [0x01, 0x01, 0x03]
            self.vm.run(bytecode)

            bytecode = [0x03, 0x17, 0x03]
            self.vm.run(bytecode)


if __name__ == '__main__':
    unittest.main()
