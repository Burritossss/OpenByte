from modules.memory import Memory
from typing import *
from modules.instructions import *

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

        self.PC = (self.memory.read(0xFFFF) << 8) | self.memory.read(0xFFFE)
        self.IR = 0x00
        self.FLAGS = 0b00000000

    def decode_instructions(self):
        '''Decodes instructions inside of Memory'''
        self.IR = self.memory.read(self.PC)

        if self.IR in INSTRUCTIONS:
            INSTRUCTIONS[self.IR](self)
        else:
            pass
            
        self.PC = (self.PC + 1) % 0x10000
        
        
        
        
