import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break
    arr = "".join(input().rstrip().split()).upper()
    
    a = dict()
    i = 0
    j = 0
    start = 0
    while True:
        if len(a) == len(arr):
            break
        if i >= len(arr):
            start += 1
            i = start
        a[i] = arr[j]
        i += n
        j += 1
    a = sorted(a.items(),key = lambda x: x[0])
    
    for i in a:
        print(i[1],end = '')
    print()