import sys 
inpit = sys.stdin.readline
import itertools

def check(lst):
    line = []
    c = 0
    ans = 0
    for i in lst:
        c += i
        line.append(c)
    for i in range(0,len(line)-1):
        for t in range(i+1,len(line)):
            if line[i] + 50 == line[t]:
                ans += 1
    return ans

ans = 0
n = int(input())
s = list(map(int, input().split(" ")))
s.sort()
if s[-1] > 50:
    print(0)
else:
    brt = list(itertools.permutations(s))
    for i in brt:
        ch = check(list(i))
        if ch > ans:
            ans = ch
    print(ans)