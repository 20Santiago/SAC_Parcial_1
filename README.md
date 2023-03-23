                     ✨ PARCIAL NÚMERO 1 ✨



###### Por: *Santiago Aguilar Cardenas*.

### **¿Qué se hizo en el parcial?**
> En el *parcial* se hizo  un programa de *Python* que calcula el ***determinante*** y la ***matriz inversa*** de una matriz cuadrada **ingresada por el usuario**.

### **¿Cómo se hizo?**

1. Se pide al usuario que ingrese el número de filas y columnas que tendrá la matriz.

2. **Se verifica si la matriz es cuadrada**. Si no es cuadrada, el programa termina y muestra un mensaje de error. Si es cuadrada, continúa ejecutando el código.

3. Se crea una matriz vacía con el número de filas y columnas ingresado por el usuario.

4. Se solicita al usuario que ingrese los valores para cada posición de la matriz.

5. Se muestra la matriz original.

6. **Se crea la matriz transpuesta**.

7. Se muestra la matriz transpuesta.

8. Se crea una matriz identidad del mismo tamaño que la matriz original.

9. Se concatena la matriz original y la matriz identidad.

10. Se convierte la matriz extendida en una matriz escalonada reducida por fila utilizando el método de eliminación de Gauss-Jordan.

11. Si se encuentra un cero en la diagonal principal durante la eliminación de Gauss-Jordan, se muestra un mensaje de error y el programa termina. Si no se encuentra ningún cero en la diagonal principal, se continúa ejecutando el código.

12. **Se extrae la matriz inversa de la matriz extendida**.

13. Se muestra la matriz inversa.