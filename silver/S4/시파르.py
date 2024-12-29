import sys
input = sys.stdin.readline

def count_zero(x):
    cnt = 0
    while x >= 5:
        x //= 5
        cnt += x
    return cnt

flag = 1
while True:
    a = int(input())
    if a == 0:
        break
    print(f"Case #{flag}: {count_zero(a)}")
    flag += 1