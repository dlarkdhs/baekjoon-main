import sys
input = sys.stdin.readline

n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
a.sort(reverse = True)
for i in a:
    print(i)