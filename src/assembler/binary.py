'''
Creates a simple binary file for editing.
Please use this for the time being when writing programs while the compiler is being written.
'''
import sys

if len(sys.argv) > 1:
    writedir = sys.argv[1]
else:
    print("Usage: python3 ./binary.py <output path>")
    sys.exit(1)

byteout:list[int] = [0x00] * 0x10000
byteout[0xFFFE] = 0x90

with open(writedir, "wb") as f:
    f.write(bytearray(byteout))