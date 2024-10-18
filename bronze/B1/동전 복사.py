import sys
input = sys.stdin.readline

n = int(input())
x,y = map(int,input().split())
ans = 4

if x == 1: ans -= 1
if y == 1: ans -= 1
if x == n: ans -= 1
if y == n: ans -= 1

print(ans)