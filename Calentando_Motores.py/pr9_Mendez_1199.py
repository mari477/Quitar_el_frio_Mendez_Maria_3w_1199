print(" ")
print("Mendez_Sanchez_Maria_Guadalupe_Yazmin_3w_1199")
print(" ")
def contar_vocales(palabra):
    #Inicializamos un diccionario para contar las vocales
    vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    #Convertimos la palabra a minúsculas para hacer la búsqueda insensible a mayúsculas
    palabra = palabra.lower()
    #Recorremos cada letra de la palabra
    for letra in palabra:
        if letra in vocales:
            vocales[letra] += 1  #Aumentamos el contador de la vocal encontrada
    return vocales
#Pedimos al usuario que ingrese una palabra
palabra_usuario = input("Ingresa una palabra para contar las vocales: ")
#Llamamos a la función para contar las vocales
resultado = contar_vocales(palabra_usuario)
#Mostramos el resultado
print("\nCantidad de vocales en la palabra:")
for vocal, cantidad in resultado.items():
    print(f"La letra '{vocal}' aparece {cantidad} veces.")
print(" ")