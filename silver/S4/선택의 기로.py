import sys
input = sys.stdin.readline

n = int(input())

arr = []
for _ in range(n):
    q,p = map(int,input().split())
    arr.append([q,p])
arr.sort(key = lambda x: (-x[0], x[1]))
print(arr[0][0],arr[0][1],arr[1][0],arr[1][1])
arr.sort(key = lambda x: x[1])
print(arr[0][0],arr[0][1],arr[1][0],arr[1][1])