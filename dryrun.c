#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// void myfunc(char** param){
// printf("%p\n", param);
// printf("%p\n", *param);
// printf("%s\n", *param);
// ++(*param);
// ++(param);
// printf("%p\n", param);
// printf("%p\n", *param);
// printf("%s\n", *param);
// // printf("%s\n", param); // ello_World
// }

// int main(){
//     char* string = (char*)malloc(64);
//     strcpy(string, "hello_World");
//     printf("Hello!! %p\n", &string);
//     printf("Venkat!! %p\n", string);
//     myfunc(&string);
//     printf("Hello!! %p\n", &string);
//     printf("venkat!! %p\n", string);
//     printf("%s\n", string); // ello_World
// }

#include <stdio.h>
void main()
{
int k = 5;
int *p = &k;
int **m = &p;
printf("%d  %d  %p\n", k, *p, **m);
}