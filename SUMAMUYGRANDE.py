from random import randint

numero_filas = int(input("elige numero de filas = "))
numero_columnas = int(input("elige numero de filas = "))

matriz = []
for i in range(numero_filas):
    matriz.append([])
    for j in range(numero_columnas):
        matriz[i].append(int(randint(0,100)))

suma = 0

for i in range(numero_filas):
    for j in range(numero_columnas):
        suma += matriz[i][j]
        suma = int(suma)

print(matriz)

print(suma)


#elementosmatriz = int(numero_filas*numero_columnas)

#for elementosmatriz in range(elementosmatriz):
    #sum(matriz[0:elementosmatriz])

#sumamatriz = sum(matriz)
#print(f"Sum of list -> {sumamatriz}")



#matrizz = [
#    [1, 2],
#    [3, 4],
#]

#def suma(matrizz):
#    sumamatriz = sum(matrizz)
#suma(matrizz)