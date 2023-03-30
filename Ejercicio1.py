print("***********************")
print("Bienvenido al programa")
print("************************\n")

#Recoleccion de datos
nombre = input("Ingrese su nombre -> ")
print(f"Bienvenido {nombre}, aqui puede ingresar la cantidad de infracciones que haya registrado\n")

registro = int(input("Ingrese la cantidad de infracciones que registro en el mes -> "))
#Obtencion del promedio de infracciones
proMat = (registro * (20/100))
proVes = (registro * (35/100))
proNoc = (registro * (45/100))

#
print(f"\nEl promedio diario matutino es de   -> {int(proMat)}")
print(f"El promedio diario vespertino es de -> {int(proVes)}")
print(f"El promedio diario nocturno es de   -> {int(proNoc)}")

print("\nFin del programna")