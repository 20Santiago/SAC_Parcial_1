# Primer parcial
# Santiago Aguilar Cardenas

# Comenzamos dandole dimensiones a la matriz dada por el usuario.
filas = int(input("Ingrese el número de filas: "))
columnas = int(input("Ingrese el número de columnas: "))

# Aplicamos un condicional para que el usuario sepa que debe de ser una matriz cuadrada.

if filas != columnas:
        print("Lo sentimos, su matriz no es cuadrada. Este programa está prediseñado para matrices cuadradas.")
else:
    
# Iniciamos con la matriz.
        matriz = []
        for i in range(filas):
            fila = []
            for j in range(columnas):
                fila.append(0)
            matriz.append(fila)

# Llenar la matriz con los valores ingresados por el usuario.
        for i in range(filas):
            for j in range(columnas):
                valor = int(input("Ingrese el valor para la posición [{}, {}]: ".format(i, j)))
                matriz[i][j] = valor

# Mostramos la matriz original.
        print("La matriz ingresada es:")
        for fila in matriz:
            print(fila)

# Se calcula la matriz transpuesta
        matriz_transpuesta = []
        for j in range(columnas):
            fila_transpuesta = []
            for i in range(filas):
                fila_transpuesta.append(matriz[i][j])
            matriz_transpuesta.append(fila_transpuesta)

# Se muestra la matriz transpuesta
        print("La matriz transpuesta es:")
        for fila in matriz_transpuesta:
                print(fila)

# Se crea una matriz identidad del mismo tamaño que la matriz original
        identidad = []
        for i in range(filas):
            fila = []
            for j in range(columnas):
                if i == j:
                    fila.append(1)
                else:
                    fila.append(0)
            identidad.append(fila)

# Concatenar la matriz original y la matriz identidad
        matriz_extendida = []
        for i in range(filas):
            fila_extendida = matriz[i] + identidad[i]
            matriz_extendida.append(fila_extendida)

# Transformar la matriz extendida en una matriz escalonada reducida por fila
        for i in range(filas):
            fila_pivote = matriz_extendida[i]
            pivote = fila_pivote[i]
            if pivote == 0:
                print("La matriz no es invertible")
                break
            else:
                for j in range(columnas * 2):
                    fila_pivote[j] = fila_pivote[j] / pivote
                matriz_extendida[i] = fila_pivote
                for k in range(filas):
                    if k != i:
                        fila_a_eliminar = matriz_extendida[k]
                        factor = fila_a_eliminar[i]
                        for j in range(columnas * 2):
                            fila_a_eliminar[j] = fila_a_eliminar[j] - factor * fila_pivote[j]
                        matriz_extendida[k] = fila_a_eliminar

# Extraer la matriz inversa de la matriz extendida
        inversa = []
        for i in range(filas):
            fila_inversa = matriz_extendida[i][columnas:]
            inversa.append(fila_inversa)

# Mostrar la matriz inversa
        print("La matriz inversa es:")
        for fila in inversa:
            print(fila)

# Calcular el determinante
        determinante = pivote
        for i in range(filas):
            fila_pivote = matriz_extendida[i]
            pivote = fila_pivote[i]
            determinante *= pivote

# Mostrar el determinante
        print("El determinante de la matriz es:", determinante)




## Ejercicio:

# Una fábrica de muebles fabrica 2 modelos de estanterias A y B, cada uno en dos tamaños grande y pequeño.
# Produce diariamente 100 estanterias grande y 800 estanterias pequeñas del tipo A, y 700 grandes y 200 pequeñas
# del tipo B. Con la información anterior, interprete la matriz, halle su transpuesta y calcule la inversa de la matriz.

# Utilice para su solución, el programa anterior.

 