import sys
input = sys.stdin.readline

m = int(input())
n = int(input())

is_prime = [True] * (n+1)
is_prime[0] = is_prime[1] = False

for i in range(2,int(n**(1/2))+1):
    if is_prime[i] == False:
        continue
    for j in range(i*i,n+1,i):
        is_prime[j] = False

primes = [i for i in range(m,n+1) if is_prime[i] == True]
if len(primes) == 0:
    print(-1)
else:
    print(sum(primes),primes[0], sep = '\n')