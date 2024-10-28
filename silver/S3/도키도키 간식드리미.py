import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
side = []

flag = 1
for i in a:
    side.append(i)
    while side and side[-1] == flag:
        side.pop()
        flag += 1
    if len(side) > 1 and side[-1] > side[-2]:
        print("Sad")
        sys.exit()
if side:
    print("Sad")
else:
    print("Nice")