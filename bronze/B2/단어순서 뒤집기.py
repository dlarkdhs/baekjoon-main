import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    arr = list(input().rstrip().split())
    print("Case #%d: %s" %(i+1,' '.join(arr[::-1])))