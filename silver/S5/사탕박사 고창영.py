import sys
input = sys.stdin.readline

t = int(input())
find1 = '>'
find2 = 'v'
for I in range(t):
    cnt = 0
    b = input()
    r,c = map(int,input().split())
    a = [input().rstrip() for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if a[i][j] == find1 and c-j >= 3:
                if a[i][j+1] == 'o' and a[i][j+2] == '<':
                    cnt += 1
            elif a[i][j] == find2 and r-i >= 3:
                if a[i+1][j] == 'o' and a[i+2][j] == '^':
                    cnt += 1
    print(cnt)