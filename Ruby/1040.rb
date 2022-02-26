n1,n2,n3,n4 = gets.chomp.split(' ').map(&:to_f)
media = (2*n1+3*n2+4*n3+1*n4)/10
puts("Media: %.1f" % [media])
if media>=7
  puts("Aluno aprovado.")
elsif media<5
  puts("Aluno reprovado.")
elsif 5<=media && media<7
  puts("Aluno em exame.")
  n5 = gets.chomp.to_f
  puts("Nota do exame: #{n5.round(1)}")
  media = (media+n5)/2
  if media>=5
    puts("Aluno aprovado.")
    puts("Media final: %.1f" % [media])
  else
    puts("Aluno reprovado.")
    puts("Media final: %.1f" % [media])
  end
end