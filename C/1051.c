#include <stdio.h>
#include <stdlib.h>

int main()
{
  float income, tax_by_8, tax_by_18, tax_by_28, result;

  scanf("%f", &income);

  if (income <= 2000)
  {
    puts("Isento");
    return 0;
  }
  else if (2000 < income && income <= 3000)
  {
    tax_by_8 = (income - 2000) * 0.08;
    result = tax_by_8;
  }
  else if (3000 < income && income <= 4500)
  {
    tax_by_8 = income - 2000 > 1000 ? 1000 * 0.08 : (income - 2000) * 0.08;
    tax_by_18 = (income - 3000) * 0.18;
    result = tax_by_8 + tax_by_18;
  }
  else
  {
    tax_by_8 = income - 2000 > 1000 ? 1000 * 0.08 : (income - 2000) * 0.08;
    tax_by_18 = income - 3000 > 1500 ? 1500 * 0.18 : (income - 3000) * 0.18;
    tax_by_28 = (income - 4500) * 0.28;
    result = tax_by_8 + tax_by_18 + tax_by_28;
  }
  printf("R$ %.2f\n", result);
  return 0;
}
