print("------------------------------")
print("----Bienvenido al programa----")
print("------------------------------")

print("\nEn este programa podras conocer el tamño de tres números")

#Definicion de variables
num1 = int(input("\nIngrese un número entero: "))
num2 = int(input("\nIngrese un número entero: "))
num3 = int(input("\nIngrese un número entero: "))

x = 9
y = 9
z = 9

if x == 9:
    if num1 > num2 and num1 > num3:
        print(f"El numero mayor es {num1}")
        numA = num1

    elif num2 > num1 and num2 > num3:
        print(f"El numero mayor es {num2}")
        numA = num2

    elif num3 > num1 and num3 > num2:
        print(f"El numero mayor es {num3}")
        numA = num3

if y == 9:
    if num1 < num2 and num1 < num3:
        print(f"El numero menor es {num1}")
        numB = num1

    elif num2 < num1 and num2 < num3:
        print(f"El numero menor es {num2}")
        numB = num2

    elif num3 < num1 and num3 < num2:
        print(f"El numero menor es {num3}")
        numB = num3

if z == 9:
    if num1 < numA and num1 > numB:
        print(f"El numero del medio es {num1}")

    elif num2 < numA and num2 > numB:
        print(f"El numero del medio es {num2}")

    elif num3 < numA and num3 > numB:
        print(f"El numero del es {num3}")

print("\nFin del programa")