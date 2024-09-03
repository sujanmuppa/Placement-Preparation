```
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
void myfunc(char** param){
++param;
}
int main(){
char* string = (char*)malloc(64);
strcpy(string, "hello_World");
myfunc(&string);
myfunc(&string);
printf("%s\n", string);
// ignore memory leak for sake of quiz
return 0;
}
```
- [ ] hello_World
- [ ] ello_World
- [ ] llo_World
- [ ] lo_World

### Answer
- [x] hello_World
- [ ] ello_World
- [ ] llo_World
- [ ] lo_World

### Explanation
- Basically the important thing here is that a pointer stores the memory address of a variable. 
- Now lets say the code is like this 
```c
void myfunc(char* param){
++param;
// printf("%s\n", param); // ello_World
}

int main(){
    char* string = (char*)malloc(64);
    strcpy(string, "hello_World");
    myfunc(string); // hello_World
}

```
What is actually happens here is that the string which stores the memory address of the starting element of the string "hello_World" is passed to the function myfunc. Now this memory address that is passed to the function is stored in the pointer param (as we discussed earlier pointers store memory addresses). Now when we do ++param, the pointer param is incremented to the next memory address. So when we print the value of param, it will print the string starting from the next memory address. 
Here the thing is the increment is done on the pointer which is local to the function myfunc. So the increment is not reflected in the main function. So when we print the string in the main function, it will print the original string.

- Now lets say the code is like this 
```c
void myfunc(char* param){
    ++(*param);
    // printf("%s\n", param); // iello_World
}

int main(){
    char* string = (char*)malloc(64);
    strcpy(string, "hello_World");
    myfunc(string); // iello_World
}
```
Now what happens here is that the value at the memory address that is stored in the pointer param is incremented. So the charecter in that memory address is incremented by 1 (with respect to the ASCII values). One thing to remember is the pointer is local to the function myfunc, but the value at the memory address is changed and this change is reflected in the main function. So when we print the string in the main function, it will print the modified string.

- Now lets say the code is like this 
```c
void myfunc(char** param){
    ++param;
    // printf("%s\n", *param); // ello_World
}

int main(){
    char* string = (char*)malloc(64);
    strcpy(string, "hello_World");
    myfunc(&string); // hello_World

}
```
Now what happens here is that the memory address of the pointer string (which is the memory address of the starting element of the string "hello_World") is passed to the function myfunc. Now this memory address that is passed to the function which is a pointer to pointer is stored in the pointer param (as we discussed earlier pointers store memory addresses). Now when we do ++param, the pointer param is incremented which actually points to a different memory address (which is previously pointing to the address of pointer which is pointing to the starting element of the string "hello_World"). so now the param is pointing to a random memory address. 

- Now lets say the code is like this 
```c
void myfunc(char** param){
    ++(*param);
    // printf("%s\n", *param); // ello_World
}

int main(){
    char* string = (char*)malloc(64);
    strcpy(string, "hello_World");
    myfunc(&string); // ello_World
}
```
Now here the same thing as above is done but the thing is now the incrimenting is done address itself. So the change is reflected in the main function. 

#### Key Takeaway: 
Whenever we work with pointers, the passing pointer will be a local variable to the function, But the things it points to will be global and the changes will be reflected in the main function.
