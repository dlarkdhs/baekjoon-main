import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    if n % 3 == 2 or n % 9 == 0:
        print("TAK")
    else:
        print("NIE")