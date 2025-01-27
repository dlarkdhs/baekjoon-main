import sys
input = sys.stdin.readline

s = input().rstrip()
a = set()
for i in range(len(s)+1):
    for j in range(i,len(s)+1):
        a.add(s[i:j])
print(len(a)-1)