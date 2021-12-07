import math
import os
import random
import re
import sys

if __name__ == "__main__":
    first_multiple_input= input().rstrip().split()


    n=int(first_multiple_input[0])

    m= int(first_multiple_input[1])

    k=int(first_multiple_input[2])

    for n_itr in range(n):
        row = input()

        #escribir nuestro código

    for k_itr in range(k):
        second_multiple_input = input().rstrip().split()

        i1 = int(second_multiple_input[0])

        j1 = int(second_multiple_input[1])

        i2 = int(second_multiple_input[2])

        j2 = int(second_multiple_input[3])

        #escribir nuestro código

lineasmapa = m
columnasmapa = n










    def restricciones():
        if m or n >= 20:
            pass
        else:
            exit()

        if i1 or i2 >= n:
            pass
        else:
            exit()

        if i1 or i2 >= m:
            pass
        else:
            exit()

        if n*m > 2*k:
            pass
        else:
            exit()

        if (i1,j1) != (i2,j2):
            pass
        else:
            exit()

        # A aparace exactamente una vez

        # Cada celda contiene como maximo una entrada a un tunel

        # Si una celda contiene una entrada a un túnel, entonces no contiene un obstáculo 


