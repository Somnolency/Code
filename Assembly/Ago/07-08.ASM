assume cs:codesg,ss:stacksg,ds:datasg

stacksg segment

	dw 0,0,0,0,0,0,0,0

stacksg ends

datasg segment
	db '1. display      '
        db '2. brows        '
        db '3. replace      '
        db '4. modify       '
datasg ends

codesg segment

start:
	mov ax,datasg
	mov ds,ax
	mov cx,4			;定义外循环层数
	mov si,0			;定义行数指针

s:
	push cx				;储存外循环层数
	mov bx,3			;恢复指针位置
	mov cx,4			;定义内循环层数
s0:
	mov al,[bx][si]
	and al,11011111b
	mov [bx][si],al
	inc bx

	loop s0

	pop cx				;取出cx
	add si,16			;换行
	loop s 				;将外循环层数减少/

	mov ax,4c00h
	int 21h

codesg ends

end start
