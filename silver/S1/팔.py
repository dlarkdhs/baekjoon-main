import sys
input = sys.stdin.readline

l,r = input().split()
cnt = 0
if len(l) != len(r):
    print(cnt)
else:
    for i in range(len(l)):
        if l[i] == "8" and r[i] == "8":
            cnt += 1
        elif l[i] != r[i]:
            break
    print(cnt)