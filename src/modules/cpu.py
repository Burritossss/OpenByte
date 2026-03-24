from memory import Memory

from typing import *

class CPU:
    def __init__(self, memory:Memory):
        self.memory = memory

        # Register Creation
        self.A:bytes # Accumulator
        self.X:bytes # X Register
        self.Y:bytes # Y Register

        self.PC:bytes # Program Counter
        self.IR:bytes # Instruction Register
        self.FLAGS:bytes # Flag Register
    
    def reset(self):
        '''Resets the CPU's variables'''
        self.A = 0x00
        self.X = 0x00
        self.Y = 0x00

        self.PC = (self.memory.read(0xFF) << 8) | self.memory.read(0xFE)
        self.IR = 0x00
        self.FLAGS = 0b00000000

    def decode_instructions(self):
        self.IR = self.memory.read()
        
        
