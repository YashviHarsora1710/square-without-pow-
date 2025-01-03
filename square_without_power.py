from os import *
from sys import *
from collections import *
from math import *

def calculateSquare(n):
    #    Write your code here
    n=abs(n)
    sum=0 
    for i in range(1,n+1):
        sum+=n
    return sum
    
n=5
calculateSquare(n)
