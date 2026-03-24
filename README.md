# OpenByte
A hackable, lightweight, 8-bit computer emulator written in python.

GENERAL INFORMATION
---
An 8-bit computer emulator written in python. It's based off of 8-bit systems of the 70's and 80's. It uses a custom written
CPU with a custom instruction set.

The purpose of this project is to create an easy to read and use 8-bit emulator that anyone can edit and share (See bottom for
[copyright information](#copyright-information)).

To clone, check out [Getting Started](#getting-started)

GETTING STARTED
--- 
Python 3+ required

For compiling, either <a href="https://pyinstaller.org/en/stable/">PyInstaller<a> is required or an alternative

First, download the project either via GIT (git clone https://github.com/Burritossss/OpenByte.git)
or just click on Code at the top, then download zip.

[WORK IN PROGRESS]

CPU INFO
---
Registers: A, X, Y, Program Counter, Instruction Register, Flags

Architecture: 8-Bit

Assembly Version: OpenByte 1.0 Pre-Alpha


EMULATOR INFORMATION
---
Language: Python

Version: 1.0.0 Pre-Alpha


MEMORY LAYOUT
---
0x0000 - 0x00FF : Stack                 - Important data like the program counter when jumping to a subroutine.

0x0100 - 0x8FFF : WRAM                  - Working Memory you can use for programs.

0x9000 - 0xFFFD : PROM                  - Read only memory for your program(s)

0xFFFE - 0xFFFF : Program Start Pointer - These two bytes tell the computer where the program starts.

High Byte then Low Byte


FLAGS
---
The FLAG register is an 8-bit register that represents the current state/status of the processor.


0 : off

1 : on

x : any number

00000000 : No flags

xxxxxxx1 : Zero Flag - Previous arithmatic equaled 0

xxxxxx1x : Negative Flag - Previous arithmatic was negative


INSTRUCTION SET
---
[WORK IN PROGRESS]




COPYRIGHT INFORMATION
---
<a href="https://github.com/Burritossss/OpenByte">OpenByte</a> © 2025 by <a href="https://github.com/Burritossss">Clayton Beatty</a> is licensed under <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International</a><img src="https://mirrors.creativecommons.org/presskit/icons/cc.svg" alt="" style="max-width: 1em;max-height:1em;margin-left: .2em;"><img src="https://mirrors.creativecommons.org/presskit/icons/by.svg" alt="" style="max-width: 1em;max-height:1em;margin-left: .2em;"><img src="https://mirrors.creativecommons.org/presskit/icons/nc.svg" alt="" style="max-width: 1em;max-height:1em;margin-left: .2em;"><img src="https://mirrors.creativecommons.org/presskit/icons/sa.svg" alt="" style="max-width: 1em;max-height:1em;margin-left: .2em;">