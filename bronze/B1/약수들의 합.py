import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == -1:
        break
    
    a = [1]
    i = 2
    for i in range(2,n//2):
        if n % i == 0:
            a.append(i)
            a.append(n//i)
    a = set(a)
    a = list(a)
    a.sort()
    if sum(a) == n:
        print(f"{n} = ", end = '')
        print(*a, sep=' + ')
    else:
        print(f"{n} is NOT perfect.")