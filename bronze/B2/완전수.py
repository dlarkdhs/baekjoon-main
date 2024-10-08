import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
A = []

for i in range(n):
    for j in range(1,a[i]):
        if a[i] % j == 0:
            A.append(j)
    if sum(A) == a[i]:
        print("Perfect")
        A.clear()
    elif sum(A) > a[i]:
        print("Abundant")
        A.clear()
    else:
        print("Deficient")
        A.clear()