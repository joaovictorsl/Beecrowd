#include <math.h>
#include <stdio.h>

int main(void)
{
  int valor;

  scanf("%i", &valor);
  printf("%i\n", valor);

  printf("%i nota(s) de R$ 100,00\n", valor / 100);
  valor = valor % 100;

  printf("%i nota(s) de R$ 50,00\n", valor / 50);
  valor = valor % 50;

  printf("%i nota(s) de R$ 20,00\n", valor / 20);
  valor = valor % 20;

  printf("%i nota(s) de R$ 10,00\n", valor / 10);
  valor = valor % 10;

  printf("%i nota(s) de R$ 5,00\n", valor / 5);
  valor = valor % 5;

  printf("%i nota(s) de R$ 2,00\n", valor / 2);
  valor = valor % 2;

  printf("%i nota(s) de R$ 1,00\n", valor / 1);

  return 0;
}
