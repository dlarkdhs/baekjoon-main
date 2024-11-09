import sys
input = sys.stdin.readline

t = int(input())

arr = []
for _  in range(t):
    n = int(input())
    for i in range(n):
        phone_number = input().rstrip()
        arr.append(phone_number)
    
# 미완