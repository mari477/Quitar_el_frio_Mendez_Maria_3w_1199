print(" ")
print("Mendez_Sanchez_Maria_Guadalupe_Yazmin_3w_1199")
print(" ")
def calcular_edad(año_actual, año_nacimiento):
    # Calculamos la edad de la persona en el año actual
    return año_actual - año_nacimiento
# Ingresamos el año en curso
año_actual = int(input("Ingresa el año en curso: "))
# Lista para almacenar la información de las personas
personas = []
# Ingresamos los datos de las tres personas
for i in range(3):
    nombre = input(f"Ingrese el nombre de la persona {i + 1}: ")
    año_nacimiento = int(input(f"Ingrese el año de nacimiento de {nombre}: "))
    edad = calcular_edad(año_actual, año_nacimiento)
    personas.append((nombre, edad))  # Guardamos el nombre y la edad calculada
# Imprimimos los resultados
print("\nEdad de las personas en el año", año_actual)
for persona in personas:
    print(f"{persona[0]} cumplirá {persona[1]} años.")
print(" ")