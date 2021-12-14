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