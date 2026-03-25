from modules.instructions import INSTRUCTIONS

class Memory:
    def __init__(self, size:bytes=0xFFFF):
        self.memory:list[bytes] = [0x00]*size
        self.size = size

    def write(self, address:bytes, value:bytes, force:bool=False):
        '''Writes to a place in memory'''
        if address > 0x9000 and not force:
            print(f'Unable to write to: {address}. Reason: Read Only.')
        else:
            self.memory[address%self.size] = value % 0x100
    
    def read(self, address:bytes):
        '''Reads a place in memory'''
        return self.memory[address%self.size] % 0x100

class CPU:
    def __init__(self, memory:Memory):
        self.memory = memory

        # Register Creation
        self.A:bytes # Accumulator
        self.X:bytes # X Register
        self.Y:bytes # Y Register

        self.PC:bytes # Program Counter
        self.IR:bytes # Instruction Register
        self.SP:bytes # Stack Pointer

        self.FLAGS:bytes # Flag Register
    
    def reset(self):
        '''Resets the CPU's variables'''
        self.A = 0x00
        self.X = 0x00
        self.Y = 0x00

        self.PC = (self.memory.read(0xFFFF) << 8) | self.memory.read(0xFFFE)
        self.IR = 0x00
        self.SP = 0x00

        self.FLAGS = 0b00000000

    def decode_instructions(self):
        '''Decodes instructions inside of Memory'''
        self.IR = self.memory.read(self.PC)

        if self.IR in INSTRUCTIONS:
            INSTRUCTIONS[self.IR](self)
        else:
            pass
        
            
