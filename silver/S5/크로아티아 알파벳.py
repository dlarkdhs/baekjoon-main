import sys
input = sys.stdin.readline


arr = ["c=","c-",'dz=','d-','lj','nj','s=','z=']
a = input().rstrip()

count = 0
i = 0
while True:
    if i == len(a):
        break
    if a[i:i+2] in arr:
        i += 2
    elif a[i:i+3] == 'dz=':
        i += 3
    else:
        i += 1
    count += 1

print(count)