import sys
input = sys.stdin.readline
from collections import deque

s = list(input().rstrip())
kor = ['K','O','R','E','A']
yon = ['Y','O','N','S','E','I']

res = deque(s)
while res:
    x = res.popleft()
    
    if x == kor[0]:
        kor.pop(0)
        if len(kor) == 0:
            print("KOREA")
            break
    if x == yon[0]:
        yon.pop(0)
        if len(yon) == 0:
            print("YONSEI")
            break
