import sys
input = sys.stdin.readline

n = int(input())
seek = "pPAp"
a = input().rstrip()

count = 0
i = 0
while True:
    if i == len(a):
        break
    if a[i:i+4] == seek:
        count += 1
        i += 4
    else:
        i += 1
print(count)