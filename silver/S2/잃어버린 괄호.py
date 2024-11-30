import sys
imput = sys.stdin.readline

s = input().rstrip()
m = s.split('-')
arr = sum(map(int,m[0].split('+')))

for i in m[1:]:
    arr -= sum(map(int, i.split('+')))
print(arr)