import sys
input = sys.stdin.readline

# 7368787
k = int(input())

a = [False,False]+[True]*7368788
num = []

for i in range(2,7368788):
    if a[i]:
        num.append(i)
        for j in range(i+i,7368788,i):
            a[j] = False
print(num[k-1])