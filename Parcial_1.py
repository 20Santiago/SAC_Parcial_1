# Primer parcial
# Santiago Aguilar Cardenas

#Comenzamos dandole dimensiones a la matriz dada por el usuario
filas = int(input("Ingrese el número de filas: "))
columnas = int(input("Ingrese el número de columnas: "))

#Creamos una condición para que el usuario sepa que debe ser una matriz cuadrada
if filas != columnas:
    print("Lo sentimos, su matriz no es cuadrada. Este programa está prediseñado para matrices cuadradas.")

else:
# Iniciamos la matriz con ceros
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(0)
        matriz.append(fila)

# Se llena la matriz con los valores ingresados por el usuario
    for i in range(filas):
        for j in range(columnas):
            valor = int(input("Ingrese el valor para la posición [{}, {}]: ".format(i, j)))
            matriz[i][j] = valor

# Se muestra la matriz
    print("La matriz ingresada es:")
    for fila in matriz:
        print(fila)