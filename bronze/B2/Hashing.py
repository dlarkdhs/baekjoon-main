import sys
input = sys.stdin.readline

n = int(input())
a = input()
arr = []

for i in a:
    arr.append(ord(i)-96)

for i in range(n):
    arr[i] = (arr[i] * 31**i)
arr.pop()
res = sum(arr)
print(res % 1234567891)