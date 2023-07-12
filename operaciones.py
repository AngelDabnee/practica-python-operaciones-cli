import os
os.system("cls")
try:
    a = float(input("escribe el valor de a "))
    b = float(input("escribe el valor de b "))
    print("El valor de lo que me pediste es ", a*b)
    print("Division", a/b)
    print("Suma",a+b)
    print("Resta",a-b)
except:
    print("solo numeros")