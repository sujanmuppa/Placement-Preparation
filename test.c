#include <stdio.h>
#include <string.h>
#include <stdlib.h>
void myfunc(char* param){
++(*param);
}
int func1(int num1){
    return ++num1;
}
int func2(int num2){
    return num2++;
}
int* func3(int* num3){
    num3++;
    return num3;
}
int* func4(int* num4){
    ++num4;
    return num4;
}
int* func5(int* num5){
    return num5++;
}
int* func6(int* num6){
    return ++num6;
}
void func7(int** num7){
    (*num7)++;
}
void func8(int** num8){
    ++(*num8);
}
int main(){
char* string = (char*)malloc(64);
strcpy(string, "hello_World");
myfunc(string);
myfunc(string);

printf("%s\n", string);

// int num1 = 10;
// printf("%d\n", func1(num1));
// printf("%d\n", func2(num1));
int arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
int* ptr = arr;
// printf("%d\n", *func5(ptr));
// printf("%d\n", *func6(ptr));
// printf("%d\n", *ptr);
// func7(&ptr);
// printf("%d\n", *ptr);
// ptr = arr;
// func8(&ptr);
// printf("%d\n", *ptr);
return 0;
}