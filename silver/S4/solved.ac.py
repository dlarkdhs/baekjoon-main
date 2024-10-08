import sys
input = sys.stdin.readline

def new_round(num):
    return int(num)+1 if num - int(num) >= 0.5 else int(num) 

n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))
a.sort()

avg = new_round(n*0.15)
cnt = n - (2*avg)

if cnt <= 0:
    print(0)
else:
    total = 0
    for i in range(avg,n-avg):
        total += a[i]
    print(new_round(total/cnt))