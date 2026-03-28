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

memory.write(0xFFFF, 0x90, True) # Write the program start High
memory.write(0xFFFE, 0x00, True) # Write the program start Low

# Initilize the cpu
cpu = CPU(memory)
cpu.reset() # and reset it

# Loop
while True:
    cpu.decode_instructions()
    if debug:
        print(f"A: {hex(cpu.a)}, X: {hex(cpu.x)}, Y: {hex(cpu.y)}, PC: {hex(cpu.pc)}, IR: {hex(cpu.ir)}, SP: {bin(cpu.sp)}")
        input("Press Enter to continue...")


