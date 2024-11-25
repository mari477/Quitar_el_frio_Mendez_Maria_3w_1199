print(" ")
print("Mendez_Sanchez_Maria_Guadalupe_Yazmin_3w_1199")
print(" ")
def contar_nombres_por_letra(nombres, letra):
    #Contamos cuántos nombres comienzan con la letra dada
    return sum(1 for nombre in nombres if nombre.lower().startswith(letra.lower()))
#Definimos una lista de nombres
nombres = ["Ana", "Pedro", "Antonio", "María", "Alfredo", "Lucía", "Alejandro", "Carlos", "Alicia", "Juan"]
print(nombres)
print(" ")
#Pedimos al usuario que ingrese una letra para buscar
letra_a_buscar = input("Ingresa la letra con la que deben comenzar los nombres: ")
#Contamos cuántos nombres empiezan con la letra proporcionada
cantidad = contar_nombres_por_letra(nombres, letra_a_buscar)
#Mostramos el resultado
print(f"\nLa cantidad de nombres que comienzan con la letra '{letra_a_buscar}' es: {cantidad}")
print(" ")