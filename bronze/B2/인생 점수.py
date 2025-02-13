import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    a = input().rstrip()
    score = 0
    for i in a:
        if i == " ":
            continue
        else:
            a_score=ord(i)-64
            score+=a_score
    if score == 100:
        print('PERFECT LIFE')
    else:
        print(score)