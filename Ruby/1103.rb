list = gets.chomp.split(' ')
h1, m1, h2, m2 = list.map &:to_i

until h1.zero? && m1.zero? && h2.zero? && m2.zero?

  mi = 60*h1+m1
  mf = 60*h2+m2
  if mi < mf
    puts(mf-mi)
  end

  if mi > mf
    puts(24*60-mi+mf)
  end

  list = gets.chomp.split(' ')
  h1, m1, h2, m2 = list.map(&:to_i)
end