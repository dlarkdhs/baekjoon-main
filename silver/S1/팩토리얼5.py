import sys
input = sys.stdin.readline

n = int(input())
fac = 1
for i in range(2,n+1):
    fac *= i
    while fac % 10 == 0:
        fac //= 10
    fac %= 10 ** (6+len(str(i)))
fac %= 100000
print(f"{'0' * (5-len(str(fac)))}{fac}")