import sys
input = sys.stdin.readline

a,b = input().split()
a,b = int(a),int(b)

att = 1
while b > a:
    if b % 2 == 0:
        b //= 2
    elif b % 10 == 1:
        b //= 10
    else:
        break
    att += 1

if b == a:
    print(att)
else:
    print(-1)