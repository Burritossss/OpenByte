from modules.components import *
import sys

debug=True

# Get the program from the argument
if len(sys.argv) == 2:
    compiledprog = sys.argv[1]
else: # Else print a usage message
    print("Usage: python main.py <path to compiled program>")
    sys.exit(0)

memory = Memory() # Initilize Memory

# Push program into memory
with open(compiledprog, 'rb') as program:
    content = program.read()
    print(f'Loaded {len(content)} bytes from {compiledprog}')
    for i, byte in enumerate(content):
        memory.write(i, byte, True)

program.close()

# Initilize the cpu
cpu = CPU(memory)
cpu.reset() # and reset it

# Loop
while True:
    cpu.decode_instructions()
    if debug:
        print(f"A: {hex(cpu.a)}, X: {hex(cpu.x)}, Y: {hex(cpu.y)}, PC: {hex(cpu.pc)}, IR: {hex(cpu.ir)}, SP: {hex(cpu.sp)}, Flags: {bin(cpu.flags)}")
        input("Press Enter to continue...")


