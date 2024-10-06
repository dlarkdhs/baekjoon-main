import sys
input = sys.stdin.readline

n = int(input())
first = list(map(int,input().split()))
second = list(map(int,input().split()))

res = []
res1 = []

for i in range(n):
    res.append(abs(first[i]))
    res1.append(abs(second[i]))
print(sum(res)+sum(res1))