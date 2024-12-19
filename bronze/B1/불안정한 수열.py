import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))

res = arr[0] % 2
cnt = 1
for i in arr[1:]:
    if i % 2 == 1 - res:
        cnt += 1
        res = 1 - res
print(cnt)