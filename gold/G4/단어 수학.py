import sys
input = sys.stdin.readline

n = int(input())
a = [input().strip() for _ in range(n)]
word = {}

for i in a:
    x = len(i)-1
    for j in i:
        if j in word:
            word[j] += 10**x
        else:
            word[j] = 10**x
        x -= 1

word = sorted(word.values(),reverse=True)
res = 0
num = 9
for i in word:
    res += i*num
    num -= 1
print(res)