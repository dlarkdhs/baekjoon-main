import sys
input = sys.stdin.readline

n = int(input())
word = [input().rstrip() for _ in range(n)]
word.sort(key=len)
cnt = 0

for i in range(n):
    flag = False
    for j in range(i+1,n):
        if word[i] == word[j][0:len(word[i])]:
            flag = True
            break
    if not flag:
        cnt += 1
print(cnt)