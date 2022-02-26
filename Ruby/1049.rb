vertebrado_dict = {
    'aguia': %w[vertebrado ave carnivoro],
    'vaca': %w[vertebrado mamifero herbivoro],
    'homem': %w[vertebrado mamifero onivoro],
    'pomba': %w[vertebrado ave onivoro]
}
invertebrado_dict = {
    'pulga': %w[invertebrado inseto hematofago],
    'lagarta': %w[invertebrado inseto herbivoro],
    'sanguessuga': %w[invertebrado anelideo hematofago],
    'minhoca': %w[invertebrado anelideo onivoro]
}

result = []
3.times do
  result.push(gets.chomp)
end

answer = result[0] == 'vertebrado' ? vertebrado_dict.key(result) : invertebrado_dict.key(result)
puts answer
