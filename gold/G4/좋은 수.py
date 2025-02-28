import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
a.sort()

res = 0
for i in range(n):
    start,end = 0,len(a)-1
    while start < end:
        if a[start] + a[end] == a[i]:
            if start == i:
                start += 1
            elif end == i:
                end -= 1
            else:
                res += 1
                break
        elif a[start] + a[end] > a[i]:
            end -= 1
        elif a[start] + a[end] < a[i]:
            start += 1
print(res)