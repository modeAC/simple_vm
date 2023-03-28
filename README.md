
# Simple VM

Simple VM implemented in Python
  * [Requirements](#requirements)
  * [Run Locally](#run-locally)
  * [Run Tests](#run-tests)
  * [Bytecode details](#bytecode-details)
  * [Other details](#other-details)
## Requirements
* [Python](https://www.python.org/) 3.8 or higher
* [pip](https://pip.pypa.io/en/stable/) 19.3.1 or higher

## Run Locally

Clone the project

```bash
  git clone https://github.com/modeAC/simple_vm.git
```

Go to the project directory

```bash
  cd simple_vm
```
Run
```bash
  python main.py
```

## Run Tests

To execute tests, run following command

```bash
  python tests.py
```

## Bytecode details
        0x00 idle:  1 byte, no ops - idle command
        0x01 load:  3 byte, 2 op   - load op1 to reg[op0]
        0x02 inc:   2 byte, 1 op   - inc reg[op]
        0x03 add:   3 byte, 2 ops  - reg[op0] = reg[op0] + reg[op1]

## Other details

To execute users bytecode initialize VM...
```bash
vm = VMProcessor()
```
...and run following (*bytecode* is a list with commands)
```bash
vm.run(bytecode)
```


