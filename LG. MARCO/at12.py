idade = int(input("Digiti sua idade: "))
if(idade <= 12 ):
    print( "criança")
elif(idade <= 17 ):
    print("Adolescente")
elif(idade <= 59 ):
    print("Adulto")
else:
    print("Idoso")