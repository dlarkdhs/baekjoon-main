import sys
input = sys.stdin.readline

n = int(input())
s = list(input().rstrip())

for i in range(n-1):
    s2 = list(input().rstrip())
    for i in range(len(s)):
        if s[i] != s2[i]:
            s[i] = "?"
print(*s,sep ='')