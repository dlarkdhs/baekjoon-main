import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    cb = cw = 0
    s1 = input()
    s2 = input()
    for i in range(n):
        if s1[i] != s2[i]:
            if s1[i] == 'B':
                cb += 1
            else:
                cw += 1
    print(max(cw,cb))