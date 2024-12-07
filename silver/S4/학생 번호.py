import sys
input = sys.stdin.readline

n = int(input())

arr = []
for _ in range(n):
    arr.append(input().rstrip())

ran = len(arr[0])
for i in range(1,ran+1):
    res = []
    for j in range(n):
        ran = arr[j][-i:]
        if ran not in res:
            res.append(ran)
        else:
            break
    if len(res) == n:
        print(i)
        break