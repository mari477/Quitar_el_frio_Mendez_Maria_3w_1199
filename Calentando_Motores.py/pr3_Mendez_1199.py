print(" ")
print("Mendez_Sanchez_Maria_Guadalupe_Yazmin_3w_1199")
print(" ")
def filtrar_palabras(lista_palabras, n):
    #Usamos una lista por comprensión para filtrar las palabras
    palabras_filtradas = [palabra for palabra in lista_palabras if len(palabra) > n]
    return palabras_filtradas
#Hacemos una lista con las palabras
palabras = ["manzana", "plátano", "kiwi", "fresa", "sandía"]
n = 5             #Elijo Que quiero poner
print(palabras)
print(" ")
print("Las palabras que van a salir seran:")
print(filtrar_palabras(palabras, n))  #Salida esperada: ['manzana', 'plátano', 'sandía']
print(" ")
