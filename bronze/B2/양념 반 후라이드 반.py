import sys
input = sys.stdin.readline

# a = 양념 b = 후라이드 c = 반반 x = 양념 마리 y = 후라이드 마리
a,b,c,x,y = map(int,input().split())
if a + b < 2 * c:
    print(a * x + b * y)
else:
    print(2 * c * min(x, y) + min(a, 2 * c) * max(0, x - y) + min(b, 2 * c) * max(0, y - x))