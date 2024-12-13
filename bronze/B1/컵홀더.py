import sys
input = sys.stdin.readline

n = int(input())
a = input().rstrip()

cnt = 0
for i in a:
    if i == "L":
        cnt += 1
if cnt // 2 < 1:
    print(n)
else:
    print(n-cnt//2+1)