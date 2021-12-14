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
    from random import randint

    def encerrada(FILA, COLUMNA):
        if FILA == 0 and tableroajedrez[FILA + 1][COLUMNA] != ' ':
            fallo = True
        elif FILA == 1:
            if tableroajedrez[FILA + 1][COLUMNA] != ' ' and tableroajedrez[FILA - 1][COLUMNA] != ' ':
            fallo = True
            else:
                fallo = False
        elif FILA == 2 and tableroajedrez[FILA - 1][COLUMNA] != ' ':
                fallo = True
        else:
            fallo = False
        return fallo

    def printeartablero(tableroajedrez):
        contador_indice = 0
        for tableroajedrez[contador_indice] in tableroajedrez:
            print(tableroajedrez[contador_indice])
            contador_indice += 1
        print("\n")
    def movimiento(FILA, COLUMNA):
    if FILA == 0:
            tableroajedrez[FILA+1][COLUMNA] = tableroajedrez[FILA][COLUMNA]
            tableroajedrez[FILA][COLUMNA] = ' '
    elif FILA == 1:
        if tableroajedrez[FILA+1][COLUMNA] != ' ':
            tableroajedrez[FILA-1][COLUMNA] = tableroajedrez[FILA][COLUMNA]
            tableroajedrez[FILA][COLUMNA] = ' '
        else:
            tableroajedrez[FILA+1][COLUMNA] = tableroajedrez[FILA][COLUMNA]
            tableroajedrez[FILA][COLUMNA] = ' '
    elif FILA == 2:
        tableroajedrez[FILA-1][COLUMNA] = tableroajedrez[FILA][COLUMNA]
        tableroajedrez[FILA][COLUMNA] = ' '

def cambio(FILA, COLUMNA):
    if FILA == 0:
        FILA = FILA + 1
    elif FILA == 1:
        if tableroajedrez[FILA+1][COLUMNA] != ' ':
            FILA = FILA - 1
        else:
            FILA = FILA + 1
    elif FILA == 2:
        FILA = FILA - 1
    return FILA
    while True:
    tableroajedrez =  [
    [' ', ' ', ' '], 
    [' ', ' ', ' '],
    [' ', ' ', ' '], 
    ]

    x = randint(0,2)
    y = randint(0,2)
    z = randint(0,2)
    a = randint(0,2)
    b = randint(0,2)
    c = randint(0,2)

    while x == a:
        a = randint(0,2)
    while y == b:
        b = randint(0,2)
    while z == c:
        c = randint(0,2)

    #posicionpiezas
    (tableroajedrez[x])[0] = chr(0x2656)
    (tableroajedrez[y])[1] = chr(0x2656)
    (tableroajedrez[z])[2] = chr(0x2656)
    (tableroajedrez[a])[0] = chr(0x265C)
    (tableroajedrez[b])[1] = chr(0x265C)
    (tableroajedrez[c])[2] = chr(0x265C)

    printeartablero(tableroajedrez)

    errorx = encerrada(x, 0)
    errory = encerrada(y, 1)
    errorz = encerrada(z, 2)
    errora = encerrada(a, 0)
    errorb = encerrada(b, 1)
    errorc = encerrada(c, 2)

    if errorx == True and errory == True and errorz == True:
        print("El jugador blanco no se puede mover, volvemos a crear el tablero")
        pass
    elif errora == True and errorb == True and errorc == True:
        print("El jugador negro no se puede mover, volvemos a crear el tablero")
        pass
    else:
        break

turno = randint(0, 1)
while True:
    if turno == 1:
        if errorx == False and errora == False:
            movimiento(x, 0)
            x = cambio(x, 0)
            errora = encerrada(a, 0)
        elif errory == False and errorb == False:
            movimiento(y, 1)
            y = cambio(y, 1)
            errorb = encerrada(b, 1)
        elif errorz == False and errorc == False:
            movimiento(z, 2)
            z = cambio(z, 2)
            errorc = encerrada(c, 2)
        elif errorx == False:
            movimiento(x, 0)
            x = cambio(x, 0)
            errora = encerrada(a, 0)
        elif errory == False:
            movimiento(y, 1)
            y = cambio(y, 1)
            errorb = encerrada(b, 1)
        elif errorz == False:
            movimiento(z, 2)
            z = cambio(z, 2)
            errorc = encerrada(c, 2)
        else:
            break
        turno = 0
    elif turno == 0:
        if errora == False and errorx == False:
            movimiento(a, 0)
            a = cambio(a, 0)
            errorx = encerrada(x, 0)
        elif errorb == False and errory == False:
            movimiento(b, 1)
            b = cambio(b, 1)
            errory = encerrada(y, 1)
        elif errorc == False and errorz == False:
            movimiento(c, 2)
            c = cambio(c, 2)
            errorz = encerrada(z, 2)
        elif errora == False:
            movimiento(a, 0)
            a = cambio(a, 0)
            errorx = encerrada(x, 0)
        elif errorb == False:
            movimiento(b, 1)
            b = cambio(b, 1)
            errory = encerrada(y, 1)
        elif errorc == False:
            movimiento(c, 2)
            c = cambio(c, 2)
            errorc = encerrada(z, 2)
        else:
            break
        turno = 1
    printeartablero(tableroajedrez)
if errorx == True and errory == True and errorz == True:
    print("El jugador blanco no se puede mover, ha ganado el jugador negro")
elif errora == True and errorb == True and errorc == True:
    print("El jugador negro no se puede mover, ha ganado el jugador blanco")

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