
#!/bin/python3

import math
import os
import random
import re
import sys

def cutTheSticks(arr):
    yliste= list(arr)
    yliste2=[]
    sonuc=[]
    while True:
        enkucuk=min(yliste)
        sonuc +=[len(yliste)]
        for i in yliste:
            i=i-enkucuk
            if i==0:
                continue
            else:
                yliste2 +=[i]
        yliste=list(yliste2)
        yliste2=[]
        if len(yliste)==0:
            return sonuc

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

    
    




