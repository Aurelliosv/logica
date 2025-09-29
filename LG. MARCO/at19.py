peso = float(input("digite seu peso: "))
altura = float(input("digite sua autura"))
media = round(peso / (altura * altura), 2)
print (media)
if(media < 18.5):
    print("abaixo do peso")
elif(media < 25):
    print("peso normal")
elif(media < 30):
    print("sobrepeso")
else:
    print("obesidade")