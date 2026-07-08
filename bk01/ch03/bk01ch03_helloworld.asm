section .data
    msg db "Hello, World!", 0 ; Define the string to print

section .text
    global _start ; Set the program entry point

_start:
    mov rax, 1          ; Set syscall to 1 (sys_write)
    mov rdi, 1          ; Set the file descriptor to 1 (stdout)
    mov rsi, msg        ; Store a pointer to the message
    mov rdx, 13         ; Store the message length
    syscall             ; Execute the system call

    mov rax, 60         ; Set syscall to 60 (sys_exit)
    mov rdi, 0          ; Set the exit code to 0
    syscall             ; Execute the system call
