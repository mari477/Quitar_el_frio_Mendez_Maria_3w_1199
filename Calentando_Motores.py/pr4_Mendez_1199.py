print(" ")
print("Mendez_Sanchez_Maria_Guadalupe_Yazmin_3w_1199")
print(" ")
def contar_mayusculas(cadena):
    #Inicializamos un contador para las letras mayúsculas
    contador = 0
    #Recorremos cada carácter de la cadena
    for caracter in cadena:
        #Si el carácter es una letra mayúscula, aumentamos el contador
        if caracter.isupper():
            contador += 1
    return contador
#Pedimos al usuario que ingrese una cadena
cadena_usuario = input("Ingresa una cadena: ")
#Llamamos a la función para contar las mayúsculas y mostramos el resultado
resultado = contar_mayusculas(cadena_usuario)
print(f"La cadena tiene {resultado} letras mayúsculas.")
print(" ")
