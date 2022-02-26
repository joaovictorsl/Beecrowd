a, b = gets.chomp.split(' ').map(&:to_i)
result = nil
if a > b
  result = (a % b).zero? ? 'Sao Multiplos' : 'Nao sao Multiplos'
else
  result = (b % a).zero? ? 'Sao Multiplos' : 'Nao sao Multiplos'
end

puts result