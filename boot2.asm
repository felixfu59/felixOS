        ;; filename: boot.asm
org 07c00h

        mov ax, cs
        mov ds, ax
        mov es, ax

hello_entry:
        mov bp, msg
        mov cx, 14              ; 显示字符长度
        mov ah, 13h            ; 在 Teletype 模式下显示字符串
        mov al, 01h            ; 光标位置不变
        mov bh, 0              ; 显示页，图形模式下 BH 必须为 0
        mov bl, 0fh            ; 文字颜色，0F 为白色
        mov dh, 0              ; 显示行
        mov dl, 0               ; 显示列
        int 10h
        ret

msg: db "shellcodes.org"
jmp $

