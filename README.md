# Ejercicio-1
El link a mi repositorio es el siguiente:
https://github.com/blancabalmori/Ejercicio-1.git

La intención de este repositorio es la de crear dos juegos. 

En el primero, dos minions se enfrentan viendo que conjunto de letras se repite más veces. El conjunto de letras de stuart empieza con consonante, y el de Kevin con vocal, finalmente, se hace un recuento y gana el minion con más repeticiones. 

El código es el siguiente:

def minion_game (cadena):
    puntuacionstuart = 0
    puntuacionkevin = 0
    vocal = 'aeiouAEIOU'
    for i in range (len(cadena)):
        if cadena[i] not in vocal:
            puntuacionstuart += (len(cadena))
        else: 
            puntuacionkevin += (len(cadena))
    print ("La puntuación de Stuart es " + puntuacionstuart + "y la puntuación de Kevin es " + puntuacionkevin)
    if puntuacionstuart > puntuacionkevin:
        print ("Ganador, Stuart")
    elif puntuacionstuart < puntuacionkevin:
        print ("Ganador, Kevin")
    else:
        print ("Empate :(")

if __name__ == "__main__":
    cadena = input ("Escoja una palabra: ")
    minion_game(cadena)

En el segundo, es una especie de ajedrez que se juega únicamente con torres en un tablero de 3x3. Las torres se colocarán en una posición aleatoria y sólo podrán ir hacia delante o hacia atrás. Gana el jugador cuyo oponente se queda sin movimientos.

El código es el siguiente:

import math
import os
import random
import re
import sys

#
# Complete the 'verticalRooks' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
# 1. INTEGER_ARRAY r1
# 2. INTEGER_ARRAY r2
#
def verticalRooks(r1, r2):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

if __name__ == '__main__':
 fptr = open(os.environ['OUTPUT_PATH'], 'w')
 t = int(input().strip())
 for t_itr in range(t):
 n = int(input().strip())
 r1 = []
 for _ in range(n):
 r1_item = int(input().strip())
 r1.append(r1_item)
 r2 = []
 for _ in range(n):
 r2_item = int(input().strip())
 r2.append(r2_item)
 result = verticalRooks(r1, r2)
 fptr.write(result + '\n')
 fptr.close()