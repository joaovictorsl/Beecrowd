teste = gets.chomp.split('.')
if teste.length <= 1
  teste = teste[0].split(',')
end
notas = teste[0].to_i
moedas = (('0.'+teste[1]).to_f*100).to_i

hundred = notas / 100
notas -= hundred * 100
fifty = notas / 50
notas -= fifty * 50
twenty = notas / 20
notas -= twenty * 20
ten = notas / 10
notas -= ten * 10
five = notas / 5
notas -= five * 5
two = notas / 2
notas -= two * 2

if notas != 0
  moedas+=notas*100
end

one = moedas / 100
moedas -= one * 100
half = moedas / 50
moedas -= half * 50
quarter = moedas / 25
moedas -= quarter * 25
tenth = moedas / 10
moedas -= tenth * 10
half_tenth = moedas / 5
moedas -= half_tenth * 5
centh = moedas / 1

puts(
  """NOTAS:
#{hundred} nota(s) de R$ 100.00
#{fifty} nota(s) de R$ 50.00
#{twenty} nota(s) de R$ 20.00
#{ten} nota(s) de R$ 10.00
#{five} nota(s) de R$ 5.00
#{two} nota(s) de R$ 2.00
MOEDAS:
#{one} moeda(s) de R$ 1.00
#{half} moeda(s) de R$ 0.50
#{quarter} moeda(s) de R$ 0.25
#{tenth} moeda(s) de R$ 0.10
#{half_tenth} moeda(s) de R$ 0.05
#{centh} moeda(s) de R$ 0.01""")