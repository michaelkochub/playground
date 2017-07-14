#include <stdio.h>

int main () {
  int a = 10;
  void* ptr;
  ptr = &a;
  printf("addr: %d\n", *(int *)ptr);

  int arr[] = {0, 1, 2, 3};
  ptr = arr;

  printf("Value at %x is %d\n", ptr, *ptr);
  ptr++;
  printf("Value at %x is %d\n", ptr, *ptr);
  return 0;
}
