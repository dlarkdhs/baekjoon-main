import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    c,v = map(int,input().split())
    print(f"You get {c//v} piece(s) and your dad gets {c%v} piece(s).")