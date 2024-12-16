import sys
input = sys.stdin.readline

n,m = map(int,input().split())

dogamN = {}
dogamS = {}
for i in range(n):
    a = input().rstrip()
    dogamN[a] = i+1
    dogamS[i+1] = a

q = []
for _ in range(m):
    q.append(input().strip('\n'))

for i in range(m):
    try:
        ans = int(q[i])
        print(dogamS.get(ans))
    except:
        print(dogamN.get(q[i]))