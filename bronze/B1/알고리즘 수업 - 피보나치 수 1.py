import sys
input = sys.stdin.readline

def fib1(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib1(n-1)+fib1(n-2)

def fib2(n):
    j = 0
    for i in range(3,n+1):
        j += 1
    return j

n = int(input())
print(fib1(n),fib2(n))