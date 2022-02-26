#include <stdio.h>

int main()
{
  int id;
  int hour;
  float salaryphour;
  scanf("%d%d%f", &id, &hour, &salaryphour);
  float salary = salaryphour * hour;
  printf("NUMBER = %d\nSALARY = U$ %.2f\n", id, salary);
  return 0;
}
