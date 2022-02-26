A, B, C = gets.chomp.split(' ').map(&:to_f).sort.reverse!

if A >= B + C
  puts 'NAO FORMA TRIANGULO'
else
  if A**2 == B**2 + C**2
    puts 'TRIANGULO RETANGULO'
  elsif A**2 > B**2 + C**2
    puts 'TRIANGULO OBTUSANGULO'
  elsif A**2 < B**2 + C**2
    puts 'TRIANGULO ACUTANGULO'
  end
  if A == B && A == C
    puts 'TRIANGULO EQUILATERO'
  elsif B == C || A == C || A == B
    puts 'TRIANGULO ISOSCELES'
  end
end
