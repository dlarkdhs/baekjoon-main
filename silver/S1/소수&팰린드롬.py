import sys
input = sys.stdin.readline

n = int(input())
m = 1000001

a = [False]+[False]+[True]*(m-2)

for i in range(2,int(m**0.5)+1):
    if a[i]:
        for j in range(i+i,m,i):
            if a[j]:
                a[j] = False

res = 0
for i in range(n,m):
    if i == 1:
        continue
    if str(i) == str(i)[::-1]:
        if a[i]:
            res = i
            break
if res == 0:
    res = 1003001
print(res)