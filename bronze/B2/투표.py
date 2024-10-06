import sys
input = sys.stdin.readline

n,m = map(int,input().split())
game = []
human = []
vote = [0] * n

for i in range(n):
    game.append(int(input()))
for i in range(m):
    human.append(int(input()))

for j in range(m):
    k = -1
    for i in range(n):
        if game[i] <= human[j]:
            k = i
            break
    vote[k] += 1
print(vote.index(max(vote))+1)