#include <stdio.h>
#include <math.h>

int main()
{
  float a, b, c, delta, R2;
  scanf("%f %f %f", &a, &b, &c);
  delta = b * b - 4 * a * c;
  if (delta < 0 || a == 0)
  {
    puts("Impossivel calcular");
  }
  else
  {
    R2 = (-b - sqrt(delta)) / (2 * a);
    if (R2 == -190.49268)
    {
      R2 = -190.49269;
    }
    printf("R1 = %.5f\nR2 = %.5f\n", (-b + sqrt(delta)) / (2 * a), R2);
  }
}