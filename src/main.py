from modules.cpu import CPU
from modules.memory import Memory

memory = Memory() # Initilize Memory

memory.write(0xFFFF, 0x90, True) # Write the program start High
memory.write(0xFFFE, 0x00, True) # Write the program start Low

program = [
    0x01, 0xFF
]

for i, byte in enumerate(program):
    memory.write(0x9000+i, byte, True)


cpu = CPU(memory)
cpu.reset()

while True:
    cpu.decode_instructions()
    print(cpu.PC)
    print(cpu.A)


