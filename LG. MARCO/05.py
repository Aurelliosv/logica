soma = 0.0
for i in range(1, 15):
    soma += float(input("Digite a media do bimestre: "))

media = soma / 2
print(round(media, 2))

if (media >= 6):
    print("APROVADO")
elif (media >= 3.0 and media < 6):
    print("RECUPERAÇÃO")
else:
    print("REPROVADO")