# OpenByte
GENERAL INFORMATION ===========================================================================================================
An 8-bit computer emulator written in python. It's based off of 8-bit systems of the 70's and 80's. It uses a custom written
CPU with a custom instruction set.

The purpose of this project is to create an easy to read and use 8-bit emulator that anyone can edit and share (See bottom for
copyright information).
===============================================================================================================================
SYSTEM INFORMATION ============================================================================================================
CPU: 8-bit
Assembly Verison: OpenByte 1.0 Pre-Alpha
Memory address size: 0x0000 - 0xFFFF or 65535
===============================================================================================================================
EMULATOR INFORMATION ==========================================================================================================
Language: Python
Version: 1.0.0 Pre-Alpha
===============================================================================================================================
MEMORY LAYOUT =================================================================================================================
0x0000 - 0x00FF : Stack                 - Important data like the program counter when jumping to a subroutine.
0x0100 - 0x8FFF : WRAM                  - Working Memory you can use for programs.
0x9000 - 0xFFFD : PROM                  - Read only memory for your program(s)
0xFFFE - 0xFFFF : Program Start Pointer - These two bytes tells the computer where the program starts.
===============================================================================================================================
INSTRUCTION SET ===============================================================================================================
[WORK IN PROGRESS]
===============================================================================================================================
COPYRIGHT INFORMATION =========================================================================================================
<a href="https://example.com">OpenByte</a> © 2025 by <a href="https://example.com">Clayton Beatty</a> is licensed under <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/">CC BY-NC-SA 4.0</a><img src="https://mirrors.creativecommons.org/presskit/icons/cc.svg" alt="" style="max-width: 1em;max-height:1em;margin-left: .2em;"><img src="https://mirrors.creativecommons.org/presskit/icons/by.svg" alt="" style="max-width: 1em;max-height:1em;margin-left: .2em;"><img src="https://mirrors.creativecommons.org/presskit/icons/nc.svg" alt="" style="max-width: 1em;max-height:1em;margin-left: .2em;"><img src="https://mirrors.creativecommons.org/presskit/icons/sa.svg" alt="" style="max-width: 1em;max-height:1em;margin-left: .2em;">