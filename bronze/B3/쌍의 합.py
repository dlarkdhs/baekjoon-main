import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    a = int(input())
    start = 1
    print(f"Pairs for %d:" % a, end=" ")
    
    for i in range((a-1)//2):
        if i != 0:
            print(',', end=' ')
        print(start,a-start, end='')
        start += 1
    print()