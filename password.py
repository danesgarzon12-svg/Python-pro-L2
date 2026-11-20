
import random

print("================================")
print("      GENERADOR DE CONTRASEÑAS")
print("================================")

elements = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

long = int(input("\nIngresa la longitud de la contraseña: "))

password = ""

for i in range(long):
    password += random.choice(elements)

print("\n================================")
print("  Tu contraseña ha sido creada")
print("================================")

print("Contraseña:", password)
print("Longitud:", len(password), "caracteres")

print("\nGracias por usar el generador.")
