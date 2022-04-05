#include <stdio.h>

int main(void)
{
  int h1, m1, h2, m2, h3, m3;
  scanf("%d%d%d%d", &h1, &m1, &h2, &m2);

  h1 *= 60;
  h2 *= 60;
  m1 += h1;
  m2 += h2;

  if (m2 <= m1)
  {
    m2 += 1440;
  }
  h3 = (m2 - m1) / 60;
  m3 = (m2 - m1) % 60;

  printf("O JOGO DUROU %i HORA(S) E %i MINUTO(S)\n", h3, m3);
  return 0;
}
