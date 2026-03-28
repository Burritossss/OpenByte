from modules.components import *
import sys
import os

global DEBUG
DEBUG=True
if len(sys.argv) > 1:
    compiledprog = sys.argv[1]
else:
    print("Usage: python main.py <path to compiled program>")
    quit()

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
    if DEBUG:
        print(f"A: {hex(cpu.A)}, X: {hex(cpu.X)}, Y: {hex(cpu.Y)}, PC: {hex(cpu.PC)}, IR: {hex(cpu.IR)}, SP: {hex(cpu.SP)}")
        input("Press Enter to continue...")


