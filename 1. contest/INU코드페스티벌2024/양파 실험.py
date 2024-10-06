import sys
input = sys.stdin.readline

n,a,b = map(int,input().split())
good = 1
bad = 1

for i in range(n):
    good += a
    bad += b
    if good < bad:
        good,bad = bad,good
    
    if good == bad:
        bad -= 1
print(good,bad)