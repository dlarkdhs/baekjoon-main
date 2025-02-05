import sys
input = sys.stdin.readline

x1,y1,p1,q1 = map(int,input().split())
x2,y2,p2,q2 = map(int,input().split())

if p1 < x2 or q1 < y2 or x1 > p2 or y1 > q2:
        print("NULL")
elif x1 == p2 or x2 == p1:
    if q1 == y2 or q2 == y1:
        print("POINT")
    else:
        print("LINE")
elif q1 == y2 or q2 == y1:
    print("LINE")
else:
    print("FACE")