import sys
input = sys.stdin.readline

def sol(x):
    ans = []
    k = 2
    while k <= x:
        if x % k == 0:
            ans.append(k)
            x /= k
        else:
            k += 1
    return ans

n = int(input())
for _ in range(n):
    num = int(input())
    d = {}
    for i in sol(num):
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    itemli = d.items()
    for item in itemli:
        print(*item)