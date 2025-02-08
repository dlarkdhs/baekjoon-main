import sys
input = sys.stdin.readline
from itertools import combinations

l,c = map(int,input().split())
a = input().split()
alp = combinations(sorted(a),l)

ans = []

for alp in alp:
    c_count, v_count = 0,0
    for j in alp:
        if j in "aeiou":
            c_count += 1
        else:
            v_count += 1
    
    if c_count >= 1 and  v_count >= 2:
        print("".join(alp))