i = 1
soma = 0
while i <= 5:
    nota = float(input(f"Digite uma nota: "))
    soma += nota
    i += 1
media = soma / 5
print(f"A média final é {media}")
