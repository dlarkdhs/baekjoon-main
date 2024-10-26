import sys
input = sys.stdin.readline

n = int(input())
a = 2
while True:
    if n % a == 0:
        print(a)
        n = n // a
    else:
        a += 1
    if n == 1:
        break