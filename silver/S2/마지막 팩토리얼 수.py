import sys
input = sys.stdin.readline

n = int(input())

fac = 1
for i in range(1,n+1):
    fac *= i

res = str(fac)
for i in range(len(res)):
    if res[-(i+1)] != "0":
        print(res[-(i+1)])
        break
    else:
        pass