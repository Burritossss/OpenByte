; OpenByte Example Program
; Three channel counter - counts up in A, X, and Y simultaneously
; and stores each value to a dedicated memory address each iteration
.org 0xFFFE
db 0x00 0x90


.org 0x9000

; Initialize registers
LDA 0x00
LDX 0x00
LDY 0x00

loop:
    ; Increment all three registers
    INA 0x01
    INX 0x01
    INY 0x01

    ; Store results to memory
    STA 0x0100
    STX 0x0101
    STY 0x0102

    ; Loop forever
    JMP loop