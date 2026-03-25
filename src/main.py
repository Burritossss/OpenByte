from modules.components import *
import sys

global DEBUG
DEBUG=False
if len(sys.argv) > 1:
    if sys.argv[1] == 'true':
        DEBUG = True

memory = Memory() # Initilize Memory

memory.write(0xFFFF, 0x90, True) # Write the program start High
memory.write(0xFFFE, 0x00, True) # Write the program start Low

program = [ # Write a program
    0x05,
    0x08, 0x90, 0x00
]

# Push program into memory
for i, byte in enumerate(program):
    memory.write(0x9000+i, byte, True)

# Initilize the cpu
cpu = CPU(memory)
cpu.reset() # and reset it

# Loop
while True:
    cpu.decode_instructions()
    if DEBUG:
        print(f"A: {cpu.A}, X: {cpu.X}, Y: {cpu.Y}, PC: {cpu.PC}, IR: {cpu.IR}")
        input("Press Enter to continue...")


