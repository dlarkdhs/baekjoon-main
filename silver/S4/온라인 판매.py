import sys
input = sys.stdin.readline

N, M = map(int, input().split())
P = [int(input()) for _ in range(M)]

price = 0
max_profit = 0

for p in sorted(set(P), reverse=True):
    profit = (
        len([x for x in P if x >= p]) * p
        if N >= len([x for x in P if x >= p])
        else N * p
    )
    if profit >= max_profit:
        price = p
        max_profit = profit

print(price, max_profit)