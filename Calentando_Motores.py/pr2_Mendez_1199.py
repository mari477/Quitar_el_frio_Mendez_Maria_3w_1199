print(" ")
print("Mendez_Sanchez_Maria_Guadalupe_Yazmin_3w_1199")
print(" ")
def mas_larga(lista_palabras):
    #Verificamos si la lista no está vacía
    if not lista_palabras:
        return None  #Retorna None si la lista está vacía
    #Inicializamos la palabra más larga con el primer elemento de la lista
    palabra_larga = lista_palabras[0]
    # Recorremos la lista de palabras
    for palabra in lista_palabras:
        #Si encontramos una palabra más larga, la actualizamos
        if len(palabra) > len(palabra_larga):
            palabra_larga = palabra   
    return palabra_larga
#Aqui ponemos las palabras en una lista
palabras = ["manzana", "plátano", "kiwi", "fresa", "sandía"]
print(palabras)    #Imprimir la lista de la palabra
print("La palabra mas larga de la lista es:")        #Imprimir la palabra
print(mas_larga(palabras))  #Salida esperada: "plátano"
print(" ")
