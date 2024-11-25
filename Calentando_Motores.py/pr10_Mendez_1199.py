print(" ")
print("Mendez_Sanchez_Maria_Guadalupe_Yazmin_3w_1199")
print(" ")
def es_bisiesto(año):
    #Un año es bisiesto si es divisible por 4, pero no por 100,
    #a menos que también sea divisible por 400.
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        return True
    else:
        return False
#Pedimos al usuario que ingrese un año
año_usuario = int(input("Ingresa un año para saber si es bisiesto: "))
#Llamamos a la función es_bisiesto() y mostramos el resultado
if es_bisiesto(año_usuario):
    print(f"El año {año_usuario} es un año bisiesto.")
else:
    print(f"El año {año_usuario} no es un año bisiesto.")
print(" ")