nomes = ["Andre", "Bruno", "Ana", "Claudio", "Amanda", "Carlos"]
nomes_com_a = []
for nome in nomes:
    if nome.startswith('A'):
        nomes_com_a.append(nome)

print("Nomes que começam com 'A':")
for nome in nomes_com_a:
    print(nome)