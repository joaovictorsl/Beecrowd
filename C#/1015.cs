using System;
using System.Globalization;

class Point
{
  private double x;

  public double X
  {
    get { return x; }
  }

  private double y;

  public double Y
  {
    get { return y; }
  }

  public Point(double x, double y)
  {
    this.x = x;
    this.y = y;
  }

  public double getDistanceFrom(Point other)
  {
    double distance = Math.Sqrt(Math.Pow(x - other.X, 2) + Math.Pow(y - other.Y, 2));
    return distance;
  }

}

class Program
{
  static void Main(string[] args)
  {
    Point p1 = getPoint();
    Point p2 = getPoint();

    double distance = p1.getDistanceFrom(p2);
    Console.WriteLine(Math.Round(distance, 4));
  }

  static Point getPoint()
  {
    NumberFormatInfo provider = new NumberFormatInfo();
    provider.NumberDecimalSeparator = ".";
    provider.NumberGroupSeparator = ",";
    string coordinates = Console.ReadLine();
    string[] point = coordinates.Split(' ');
    double x = Convert.ToDouble(point[0], provider);
    double y = Convert.ToDouble(point[1], provider);
    return new Point(x, y);
  }
}
