import sys
input = sys.stdin.readline
import math

def isprime(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

n = int(input())
for _ in range(n):
    a = int(input())
    if a == 0 or a == 1:
        print(2)
    else:
        while True:
            if isprime(a):
                print(a)
                break
            a += 1