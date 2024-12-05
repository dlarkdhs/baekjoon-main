import sys
input = sys.stdin.readline

a = list(map(int,input().split()))
if a[0] > 100 or a[1] > 100 or a[2] > 200 or a[3] > 200 or a[4] > 300 or a[5] > 300 or a[6] > 400 or a[7] > 400 or a[8] > 500:
    print("hacker")
elif sum(a) < 100:
    print("none")
else:
    print("draw")