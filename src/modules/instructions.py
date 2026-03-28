from typing import *
import modules.components as components


# Initiate the instructions variable
global INSTRUCTIONS
INSTRUCTIONS:dict[bytes:Callable]

def nop(cpu:components.CPU):
    '''No Operation'''
    cpu.PC = (cpu.PC + 1) % 0x10000

def lda(cpu:components.CPU):
    '''Load the Accumulator with the next value in memory'''
    cpu.PC = (cpu.PC + 1) % 0x10000
    cpu.A = cpu.memory.read(cpu.PC)
    cpu.PC = (cpu.PC + 1) % 0x10000

def sta(cpu:components.CPU):
    '''Stores the accumulator at a memory address specified by the next two memory addresses'''
    cpu.PC = (cpu.PC + 1) % 0x10000

    low = cpu.memory.read(cpu.PC)
    cpu.PC = (cpu.PC + 1) % 0x10000
    high = cpu.memory.read(cpu.PC)
    address = (low << 8) | high
    cpu.memory.write(address, cpu.A)

    cpu.PC = (cpu.PC + 1) % 0x10000

def ina(cpu:components.CPU):
    '''Increment the A register'''
    cpu.PC = (cpu.PC + 1) % 0x10000
    cpu.A = (cpu.A + cpu.memory.read(cpu.PC)) % 0x100
    
    cpu.PC = (cpu.PC + 1) % 0x10000

def ldx(cpu:components.CPU):
    '''Load the X register with the next value in memory'''
    cpu.PC = (cpu.PC + 1) % 0x10000
    cpu.X = cpu.memory.read(cpu.PC)
    cpu.PC = (cpu.PC + 1) % 0x10000

def stx(cpu:components.CPU):
    '''Stores the X register at a memory address specified by the next two memory addresses'''
    cpu.PC = (cpu.PC + 1) % 0x10000

    low = cpu.memory.read(cpu.PC)
    cpu.PC = (cpu.PC + 1) % 0x10000
    high = cpu.memory.read(cpu.PC)
    address = (low << 8) | high
    cpu.memory.write(address, cpu.X)

    cpu.PC = (cpu.PC + 1) % 0x10000

def inx(cpu:components.CPU):
    '''Increment the X register'''
    cpu.X = (cpu.X + 1) % 0x100

    cpu.PC = (cpu.PC + 1) % 0x10000
    

def ldy(cpu:components.CPU):
    '''Load the Y register with the next value in memory'''
    cpu.PC = (cpu.PC + 1) % 0x10000
    cpu.Y = cpu.memory.read(cpu.PC)

    cpu.PC = (cpu.PC + 1) % 0x10000

def sty(cpu:components.CPU):
    '''Stores the Y register at a memory address specified by the next two memory addresses'''
    cpu.PC = (cpu.PC + 1) % 0x10000

    low = cpu.memory.read(cpu.PC)
    cpu.PC = (cpu.PC + 1) % 0x10000
    high = cpu.memory.read(cpu.PC)
    address = (low << 8) | high
    cpu.memory.write(address, cpu.Y)

    cpu.PC = (cpu.PC + 1) % 0x10000

def iny(cpu:components.CPU):
    '''Incremenet the Y register'''
    cpu.Y = (cpu.Y + 1) % 0x100
    cpu.PC = (cpu.PC + 1) % 0x10000

def jmp(cpu:components.CPU):
    '''Jump to the address defined in the next two bytes'''
    cpu.PC = (cpu.PC + 1) % 0x10000
    low = cpu.memory.read(cpu.PC)
    cpu.PC = (cpu.PC + 1) % 0x10000
    high = cpu.memory.read(cpu.PC)
    address = (low << 8) | high
    cpu.PC = address


INSTRUCTIONS = {
                0x00:nop,
                0x01:lda,
                0x02:sta,
                0x03:ina,
                0x11:ldx,
                0x12:stx,
                0x13:inx,
                0x21:ldy,
                0x22:sty,
                0x23:iny,
                0x61:jmp,        
                }