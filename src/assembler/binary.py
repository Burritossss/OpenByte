'''
Creates a simple binary file for editing.
Please do not use this unless you hate yourself and love writing in pure bytes
'''
import sys

if len(sys.argv) == 2:
    writedir = sys.argv[1]
else:
    print("Usage: python3 ./binary.py <output path>")
    sys.exit(1)

byteout:list[int] = [0x00] * 0x10000
byteout[0xFFFF] = 0x90

with open(writedir, "wb") as f:
    f.write(bytearray(byteout))