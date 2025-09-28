; ------------------------------------------------------------
; 65C02 starter (ca65) — 32 KiB ROM at $8000 .. $FFFF
; Build: ld65 emits build/rom.bin (exactly 32768 bytes)
; ------------------------------------------------------------

.setcpu "65C02"

.segment "CODE"

; --- Reset entry ---
RESET:
        sei                 ; mask IRQs
        cld                 ; clear decimal mode
        ldx #$FF
        txs                 ; init stack

        jsr init
        jsr main

forever:
        jmp forever

; --- Init hardware here ---
init:
        rts

; --- Your program ---
main:
        ; put your code here
        rts

; --- Interrupt stubs ---
NMI:
        rti
IRQ:
        rti

; --- Vectors placed by VECTORS segment at $FFFA..$FFFF ---
.segment "VECTORS"
        .word NMI          ; $FFFA/$FFFB
        .word RESET        ; $FFFC/$FFFD
        .word IRQ          ; $FFFE/$FFFF
