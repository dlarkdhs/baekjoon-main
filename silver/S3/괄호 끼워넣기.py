import sys
input = sys.stdin.readline

s = input().rstrip()
op = 0
cl = 0

for i in s:
    if i == "(":
        op += 1
    else:
        if op > 0:
            op -= 1
        else:
            cl += 1
print(op+cl)