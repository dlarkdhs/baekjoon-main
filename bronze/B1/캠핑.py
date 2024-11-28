import sys
input = sys.stdin.readline

# 연속하는 p일 중 l일만 사용 가능 (휴가 v일) 
cnt = 1
while True:
    l,p,v = map(int,input().split())
    if l == 0 and p == 0 and v == 0:
        break
    res = v // p
    res1 = v % p
    if res1 > l:
        print(f"Case {cnt}: {(1+res)*l}")
    else:
        print(f"Case {cnt}: {res1+res*l}")
    cnt += 1