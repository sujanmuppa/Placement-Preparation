@vishnusingh4118
3 years ago (edited)
28:24 exec() and fork() system calls.
So let's continue with this model where we said the shell itself is written as an application and the OS provides certain interfaces to allow the shell to start another program. so what are these interfces ? 
ans : fork() and exec() system calls. These sys calls are used to start another program.

34:04
Program - An executable on disk (it exists as an executable file on disk)
Process - A running program
The exec() system call converts a program to a process. 

38:00
In fact, these system calls, fork() and exec() can be used by any application. In this model, the 'Shell' is just any other application and the kernel doesn't even know it's a 'Shell' or anything special, meaning, the system calls fork() and exec() can be just as well invoked from another application. So any application, when it calls fork() creates replica processes of the parent process. When it calls exec(), loads the file into the current process. (washing out the previous process, the one that called exec() )

38:27  How to decide ? 
The programs returned by fork() are completely identical. How do you decide I'm the child and thus I should call exec() ( or exit() etc ) or I'm the parent and I should display the shell ? 
The fork() system call returns 2 processes. The child process behaves as if it has just returned from a fork() system call. 
fork() is a system call that is called by 1 process, but returns 2 processes, both at exactly the same program counter.BUT DIFFERENT pIDs (process IDs ). In the parent process, the return value of the fork() system call is the pID of the child. The child will return 0 ( or some number that cannot be a pID ). And that's your basis for distinguishing between the two processes and taking further action.

The return value of the fork() system call is a pid. The return values are different for the parent and the child. 
For the parent process, the return value of fork() is the pid of the child. For the child process, the return value is some number that can't be a PID. 

sO all that a programmer needs to do is check the return value. If the return value (from fork() system call ) is 0, then I will call exec(). If the return value is non-zero, then I will call the print the next command prompt. 

42:02 The formal code for the 'Shell' program.

45:18 Let's understand to implement the readCommand() in the shell. (high density gyaan from here til end. Watch full. gyaan includes - open, read, write, close interface exposed by UNIX system to manage access to shared resources. etc ) How smartly the OS designer has used the open(), read(), write(), close() system calls to read and write to the devices, and not just to the  files.