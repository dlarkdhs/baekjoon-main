import  sys
input = sys.stdin.readline
import math

n = int(input())
a = list(map(int,input().split()))
x = int(input())

cnt = 0
s = 0
for i in a:
    if math.gcd(x,i) == 1:
        s += i
        cnt += 1
print(s/cnt)