from modules.components import *
import modules.gui
import sys

global DEBUG
DEBUG=False
if len(sys.argv) > 1:
    if sys.argv[1] == 'true' or 'True':
        DEBUG = True

memory = Memory() # Initilize Memory

memory.write(0xFFFF, 0x90, True) # Write the program start High
memory.write(0xFFFE, 0x00, True) # Write the program start Low

# Write a program
program = [ 
    0x03, 0xFE,
    0x61, 0x90, 0x00
]

# Push program into memory
for i, byte in enumerate(program):
    memory.write(0x9000+i, byte, True)

# Initilize the cpu
cpu = CPU(memory)
cpu.reset() # and reset it

# Loop
while True:
    if DEBUG:
        print(f"A: {hex(cpu.A)}, X: {hex(cpu.X)}, Y: {hex(cpu.Y)}, PC: {hex(cpu.PC)}, IR: {hex(cpu.IR)}, SP: {hex(cpu.SP)}")
        input("Press Enter to continue...")
    cpu.decode_instructions()


