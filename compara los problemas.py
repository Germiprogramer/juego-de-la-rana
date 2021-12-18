import math
import os
import random
import re
import sys

notas1 = [73, 67, 38, 33]


for i in range(len(notas1)):
    if notas1[i]> 40:
        print("El alumno {} ha aprobado".format(i+1))
    else:
        print("El alumno {} ha suspendido".format(i+1))

for i in range(len(notas1)):
    if notas1[i]> 40:
        cociente= int(notas1[1]/5 +1)
        multiplo = cociente*5
        if (multiplo-notas1[i]) <3:
            print("La nota del alumno {} se aproxima, la nota es {}".format(i+1,multiplo))
    elif notas1[i]< 40:
        print("El alumno {} se queda con su nota".format(i+1,notas1[i]))
    else:
        print("El alumno {} se queda con su nota".format(i+1,notas1[i]))
    