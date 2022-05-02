import java.util.Scanner;

public class Beecrowd1021 {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    double totalValue = sc.nextDouble();
    sc.close();
    double[] bills = { 100.00, 50.00, 20.00, 10.00, 5.00, 2.00 };
    double[] coins = { 1.00, 0.50, 0.25, 0.10, 0.05, 0.01 };
    System.out.println("NOTAS:");
    for (double bill : bills) {
      double[] answer = calcAnswer(totalValue, bill);
      totalValue = answer[0];
      printAnswer((int) answer[1], bill);
    }
    System.out.println("MOEDAS:");
    for (double coin : coins) {
      double[] answer = calcAnswer(totalValue, coin);
      totalValue = answer[0];
      printAnswer((int) answer[1], coin);
    }
  }

  public static double[] calcAnswer(double totalValue, double divisor) {
    boolean smallNumber = divisor < 1;
    if (smallNumber) {
      totalValue *= 100;
      divisor *= 100;
    }
    int amount = (int) (totalValue / divisor);
    totalValue -= amount * divisor;
    if (smallNumber) {
      totalValue /= 100;
      divisor /= 100;
    }
    double[] answer = { totalValue, amount };
    return answer;
  }

  public static void printAnswer(int amount, double value) {
    String kind = value > 1 ? "nota(s)" : "moeda(s)";
    System.out.printf("%d %s de R$ %.2f\n", amount, kind, value);
  }
}
