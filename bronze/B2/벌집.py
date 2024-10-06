import sys
input = sys.stdin.readline

n = int(input())
room = 1
cnt = 1
while True:
    if n == 1:
        print(1)
        break
    
    room += 6 * cnt
    cnt += 1
    if room >= n:
        print(cnt)
        break