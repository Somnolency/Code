assume cs:code
code segment

mov ax,76ah

mov ds,ax
mov ax,20h
mov es,ax
mov bx,0

mov cx,18h

s:      mov al,[bx]
        mov es:[bx],al
        inc bx
        loop s
mov ax,4c00h
int 21h
code ends
end
