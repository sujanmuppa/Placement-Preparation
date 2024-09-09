#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>

int main() {
    int pipe1[2]; // Pipe between sort and uniq
    int pipe2[2]; // Pipe between uniq and wc

    // Create the first pipe
    if (pipe(pipe1) == -1) {
        perror("pipe1 failed");
        exit(1);
    }

    // Fork the first child for "sort file.txt"
    pid_t pid1 = fork();
    if (pid1 == -1) {
        perror("fork1 failed");
        exit(1);
    }

    if (pid1 == 0) {
        // In the first child process: run "sort file.txt"
        // Redirect stdout to write to pipe1
        close(pipe1[0]); // Close unused read end of pipe1
        dup2(pipe1[1], STDOUT_FILENO); // Redirect stdout to pipe1[1]
        close(pipe1[1]); // Close pipe1[1] after redirection

        // Execute "sort file.txt"
        execlp("sort", "sort", "file.txt", (char *)NULL);
        perror("execlp sort failed");
        exit(1);
    }

    // Create the second pipe
    if (pipe(pipe2) == -1) {
        perror("pipe2 failed");
        exit(1);
    }

    // Fork the second child for "uniq"
    pid_t pid2 = fork();
    if (pid2 == -1) {
        perror("fork2 failed");
        exit(1);
    }

    if (pid2 == 0) {
        // In the second child process: run "uniq"
        // Redirect stdin to read from pipe1, stdout to write to pipe2
        close(pipe1[1]); // Close unused write end of pipe1
        dup2(pipe1[0], STDIN_FILENO); // Redirect stdin to pipe1[0]
        close(pipe1[0]); // Close pipe1[0] after redirection

        close(pipe2[0]); // Close unused read end of pipe2
        dup2(pipe2[1], STDOUT_FILENO); // Redirect stdout to pipe2[1]
        close(pipe2[1]); // Close pipe2[1] after redirection

        // Execute "uniq"
        execlp("uniq", "uniq", (char *)NULL);
        perror("execlp uniq failed");
        exit(1);
    }

    // Fork the third child for "wc"
    pid_t pid3 = fork();
    if (pid3 == -1) {
        perror("fork3 failed");
        exit(1);
    }

    if (pid3 == 0) {
        // In the third child process: run "wc"
        // Redirect stdin to read from pipe2
        close(pipe2[1]); // Close unused write end of pipe2
        dup2(pipe2[0], STDIN_FILENO); // Redirect stdin to pipe2[0]
        close(pipe2[0]); // Close pipe2[0] after redirection

        // Execute "wc"
        execlp("wc", "wc", (char *)NULL);
        perror("execlp wc failed");
        exit(1);
    }

    // In the parent process: close all pipes
    close(pipe1[0]);
    close(pipe1[1]);
    close(pipe2[0]);
    close(pipe2[1]);

    // Wait for all children to finish
    wait(NULL);
    wait(NULL);
    wait(NULL);

    return 0;
}
