import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))

cnt = 0
start = 0
fruit = {}
dis_cnt = 0

for end in range(n):
    if a[end] in fruit:
        fruit[a[end]] += 1
    else:
        fruit[a[end]] = 1
        dis_cnt += 1
    
    while dis_cnt > 2:
        fruit[a[start]] -= 1
        if fruit[a[start]] == 0:
            del fruit[a[start]]
            dis_cnt -= 1
        start += 1
    cnt = max(cnt,end-start+1)
print(cnt)