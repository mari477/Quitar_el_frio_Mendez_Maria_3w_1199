print(" ")
print("Mendez_Sanchez_Maria_Guadalupe_Yazmin_3w_1199")
print(" ")
def binario_a_entero(binario):
    #Convertimos el número binario (cadena) a entero usando la función int() con base 2
    return int(binario, 2)
#Pedimos al usuario que ingrese un número binario
numero_binario = input("Ingresa un número binario: ")
#Llamamos a la función para convertir el binario a entero
resultado = binario_a_entero(numero_binario)
#Mostramos el resultado
print(f"El número binario {numero_binario} es igual a {resultado} en decimal.")
print(" ")