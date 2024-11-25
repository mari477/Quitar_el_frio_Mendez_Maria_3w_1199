print(" ")
print("Mendez_Sanchez_Maria_Guadalupe_Yazmin_3w_1199")
print(" ")
def max_in_list(lista):
    # Verificamos si la lista no está vacía
    if not lista:
        return None  # Retorna None si la lista está vacía
    # Inicializamos el máximo con el primer valor de la lista
    max_num = lista[0]
    # Recorremos la lista comparando cada número con el actual máximo
    for num in lista:
        if num > max_num:
            max_num = num  # Actualizamos el máximo si encontramos un número mayor
    return max_num
numeros = [5, 3, 8, 1, 9, 4]
print(numeros)                     #Imprimir la lista
print("El numero mas grande es:")   #Imprimir cual es el numero mas grande de la lista
print(max_in_list(numeros))          #Salida esperada: 9
print(" ")
