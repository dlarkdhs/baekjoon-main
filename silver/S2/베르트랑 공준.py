import sys
import math

data = []

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    else:
        data.append(n)

y = 123456 * 2
arr = [True for _ in range(y+1)]
arr[1] = False

for i in range(2, int(math.sqrt(y))+1):
    if arr[i]:
        j = 2
        while i * j <= y:
            arr[i*j] = False
            j += 1


for x in data:
    count = 0

    for i in range(x+1, 2*x+1):
        if arr[i]:
            count += 1

    print(count)