import sys
input = sys.stdin.readline

n = input()
n = n.replace("\n","")
cnt = 0
while len(n) > 1:
    res = 1
    for i in n:
        res *= int(i)
    n = str(res)
    cnt += 1
print(cnt)