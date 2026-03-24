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