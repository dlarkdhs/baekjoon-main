import sys
input = sys.stdin.readline

count = 0
while True:
    try:
        N,M = map(int,input().split())
        for i in range(N, M+1):
            num = str(i)
            numList = list(num)
            numSet = set(numList)
            if len(numList) == len(numSet):
                count += 1
        print(count)
        count = 0
    except ValueError:
        break