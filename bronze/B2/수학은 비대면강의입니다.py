import sys
input = sys.stdin.readline

a,b,c,d,e,f = map(int,input().split())
print(int((c*e-f*b)/(a*e-d*b)),int((c*d-a*f)/(b*d-a*e)))