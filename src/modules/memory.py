class Memory:
    def __init__(self, size:bytes=0xFFFF):
        self.memory:list[bytes] = [0x00]*size
        self.size = size

    def write(self, address:bytes, value:bytes):
        self.memory[address%self.size+1] = value % 0x100
    
    def read(self, address:bytes):
        return self.memory[address%self.size+1]