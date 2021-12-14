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