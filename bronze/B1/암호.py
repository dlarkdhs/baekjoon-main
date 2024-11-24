import sys
input = sys.stdin.readline

k = int(input())
pw = list(input().rstrip())

arr = []
for i in range(len(pw)):
    if i % k == 0:
        if i % 2 == 0:
            arr.append(pw[i:i+k])
        else:
            arr.append(list(reversed(pw[i:i+k])))

res = []
for i in range(k):
    for j in range(len(arr)):
        res.append(arr[j][i])
print(''.join(map(str,res)))