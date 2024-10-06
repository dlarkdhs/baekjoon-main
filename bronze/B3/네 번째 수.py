import sys
input = sys.stdin.readline

num = list(map(int,input().split()))
num.sort()
d = min(num[1]-num[0],num[2]-num[1])
for i in range(3):
    tem = num[i]
    if tem + d not in num:
        print(tem+d)
        break