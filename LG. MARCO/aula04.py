a = int(input("Digiti um valor para A: "))
b =  int(input("Digiti um valor para B: "))
c = int(input("Digiti um valor para C: "))

if (a>b and a>c):
    print("A é o maior")
elif(b>c):
    print("B é o maior" )
elif(c>b and c>a):
    print("C é o maior")
else:
    print("São iguais")

