import sys
input = sys.stdin.readline

while True:
    try:
        n,k = map(int,input().split())
        res = n
        while n//k:
            res += n//k
            n = n//k+n%k
        print(res)
    except:
        break