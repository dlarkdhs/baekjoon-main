import sys
input = sys.stdin.readline

n = int(input())

sing = 1
cnt = 1
sec = 0
while n != 0:
    if sing > n:
        sing = 1
        cnt = 1
    n -= cnt
    cnt += 1
    sing += 1
    sec += 1
print(sec)