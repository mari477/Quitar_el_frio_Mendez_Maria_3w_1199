print(" ")
print("Mendez_Sanchez_Maria_Guadalupe_Yazmin_3w_1199")
print(" ")
def contar_edades_superiores_a_20(edades):
    #Contamos cuántas edades son mayores a 20
    return sum(1 for edad in edades if edad > 20)
#Creamos una lista vacía para ingresar las edades
edades = []
#Pedimos al usuario que ingrese las edades de 10 personas
for i in range(10):
    edad = int(input(f"Ingrese la edad de la persona {i + 1}: "))
    edades.append(edad)  #Añadimos la edad a la lista
#Convertimos la lista de edades en una tupla
edades_tupla = tuple(edades)
#Contamos cuántas personas tienen edades superiores a 20
cantidad_mayores_20 = contar_edades_superiores_a_20(edades_tupla)
#Mostramos el resultado
print(f"\nLa cantidad de personas con edades superiores a 20 es: {cantidad_mayores_20}")
print(" ")