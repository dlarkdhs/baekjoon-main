import sys
input = sys.stdin.readline

n,l,w,h = map(int,input().split())

left = 0
right = max(l,w,h)

for _ in range(1000):
    mid = (left+right)/2
    if (l//mid) * (w//mid) * (h//mid) >= n:
        left = mid
    else:
        right = mid
print(f"{mid:.10f}")