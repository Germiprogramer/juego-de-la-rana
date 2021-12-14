from random import randint
import numpy as np
np.array([1,2],[3,4])

print(np.array([1,2],[3,4]))

matriz = [
    [1, 2],
    [3, 4],
]



def suma(matriz):
    sumamatriz = (matriz[0])[0] + (matriz[1])[0] + (matriz[0])[0] + (matriz[0])[1]
    print(sumamatriz)
    
suma(matriz)