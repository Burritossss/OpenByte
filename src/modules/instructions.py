from typing import *
# from modules.cpu import CPU

# Go to the very bottom to modify the instructions!

# Initiate the instructions variable
global INSTRUCTIONS
INSTRUCTIONS:dict[bytes:Callable]

def lda(cpu):
    '''Load the Accumulator with the next value in memory'''
    cpu.PC+=1
    cpu.A = cpu.memory.read(cpu.PC)


INSTRUCTIONS = {0x01:lda}