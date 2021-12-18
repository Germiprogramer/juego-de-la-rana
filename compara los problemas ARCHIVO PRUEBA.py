from math import atan2
from random import randint

a1 = randint(0,100)
a2 = randint(0,100)
a3 = randint(0,100)
b1 = randint(0,100)
b2 = randint(0,100)
b3 = randint(0,10)

print("Las notas de Lucía son>>\nCLARIDAD DEL PROBLEMA = {} \nORIGINALIDAD = {} \nDIFICULTAD = {}".format(a1,a2,a3))
print("Las notas de Carlos son>>\nCLARIDAD DEL PROBLEMA = {} \nORIGINALIDAD = {} \nDIFICULTAD = {}".format(b1,b2,b3))


a = [a1, a2, a3]
b = [a2, b2, b3]

def compareTriplets():
    puntos_lucia = 0
    puntos_carlos = 0
    
    if a[0] > b[0]:
        puntos_lucia += 1
    elif a[0] < b[0]:
        puntos_carlos += 1
    else:
        pass

    if a[1] > b[1]:
        puntos_lucia += 1
    elif a[1] < b[1]:
        puntos_carlos += 1
    else:
        pass

    if a[2] > b[2]:
        puntos_lucia += 1
    elif a[2] < b[2]:
        puntos_carlos += 1
    else:
        pass

    print("[{},{}]".format(puntos_lucia,puntos_carlos))
    return

compareTriplets()