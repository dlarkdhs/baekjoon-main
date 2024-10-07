import sys
input = sys.stdin.readline

# score = (s*(1+1/a)*(1+m/t))/4
n = int(input())
res = 0
for i in range(n):
    s,a,t,m = map(float,input().split())
    score = (s*(1+1/a)*(1+m/t))/4
    res += score
res_score = round(res,2)

p = int(input())
p_score = []
for i in range(p):
    r = float(input())
    p_score.append(r)
p_score.append(res_score)
p_score.sort(reverse=True)

rank = p_score.index(res_score)+1
result = (p+1)*0.15

if rank <= result:
    print(f'The total score of Younghoon "The God" is {res_score:.2f}.')
else:
    print(f'The total score of Younghoon is {res_score:.2f}.')