from typing import *

# Create basic versions of the actual components so that you can see the functions and variables
if True:
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

# Go to the very bottom to modify the instructions!

# Initiate the instructions variable
global INSTRUCTIONS
INSTRUCTIONS:dict[bytes:Callable]

def lda(cpu:CPU):
    '''Load the Accumulator with the next value in memory'''
    cpu.PC = (cpu.PC + 1) % 0x10000
    cpu.A = cpu.memory.read(cpu.PC)
    cpu.PC = (cpu.PC + 1) % 0x10000

def sta(cpu:CPU):
    '''Stores the accumulator at a memory address specified by the next two memory addresses'''
    cpu.PC = (cpu.PC + 1) % 0x10000

    low = cpu.memory.read(cpu.PC)
    cpu.PC = (cpu.PC + 1) % 0x10000
    high = cpu.memory.read(cpu.PC)
    address = (low << 8) | high
    cpu.memory.write(address, cpu.A)

    cpu.PC = (cpu.PC + 1) % 0x10000

def ina(cpu:CPU):
    '''Increment the A register'''
    cpu.PC = (cpu.PC + 1) % 0x10000
    cpu.A = (cpu.A + cpu.memory.read(cpu.PC)) % 0x100
    
    cpu.PC = (cpu.PC + 1) % 0x10000

def ldx(cpu:CPU):
    '''Load the X register with the next value in memory'''
    cpu.PC+=1
    cpu.X = cpu.memory.read(cpu.PC)
    cpu.PC = (cpu.PC + 1) % 0x10000

def stx(cpu:CPU):
    '''Stores the X register at a memory address specified by the next two memory addresses'''
    cpu.PC = (cpu.PC + 1) % 0x10000

    low = cpu.memory.read(cpu.PC)
    cpu.PC = (cpu.PC + 1) % 0x10000
    high = cpu.memory.read(cpu.PC)
    address = (low << 8) | high
    cpu.memory.write(address, cpu.X)

    cpu.PC = (cpu.PC + 1) % 0x10000

def inx(cpu:CPU):
    '''Increment the X register'''
    cpu.X = (cpu.X + 1) % 0x100000

    cpu.PC = (cpu.PC + 1) % 0x10000
    

def ldy(cpu:CPU):
    '''Load the Y register with the next value in memory'''
    cpu.PC+=1
    cpu.Y = cpu.memory.read(cpu.PC)

    cpu.PC = (cpu.PC + 1) % 0x10000

def sty(cpu:CPU):
    '''Stores the Y register at a memory address specified by the next two memory addresses'''
    cpu.PC = (cpu.PC + 1) % 0x10000

    low = cpu.memory.read(cpu.PC)
    cpu.PC = (cpu.PC + 1) % 0x10000
    high = cpu.memory.read(cpu.PC)
    address = (low << 8) | high
    cpu.memory.write(address, cpu.Y)

    cpu.PC = (cpu.PC + 1) % 0x10000

def iny(cpu:CPU):
    '''Incremenet the Y register'''
    cpu.Y = (cpu.Y + 1) % 0x100000
    cpu.PC = (cpu.PC + 1) % 0x10000

def jmp(cpu:CPU):
    '''Jump to the address defined in the next two bytes'''
    cpu.PC+=1
    low = cpu.memory.read(cpu.PC)
    cpu.PC+=1
    high = cpu.memory.read(cpu.PC)
    address = (low << 8) | high
    cpu.PC = address


INSTRUCTIONS = {0x01:lda,
                0x02:sta,
                0x03:ina,
                0x11:ldx,
                0x12:stx,
                0x13:inx,
                0x21:ldy,
                0x22:sty,
                0x23:iny,
                
                }