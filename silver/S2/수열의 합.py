import sys
input = sys.stdin.readline

n,l = map(int,input().split())

for i in range(l,101):
    a = n-(i*(i+1)//2)
    if a % i == 0:
        A = a // i
        if A + 1 >= 0:
            print(*(i for i in range(A+1,A+i+1)))
            break
else:
    print(-1)