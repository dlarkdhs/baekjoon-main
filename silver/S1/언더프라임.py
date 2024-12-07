import sys
input = sys.stdin.readline
import math

def sosu(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(math.sqrt(limit)) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return is_prime

def cut(n, primes):
    count = 0
    for prime in primes:
        if prime * prime > n:
            break
        while n % prime == 0:
            count += 1
            n //= prime
    if n > 1:
        count += 1
    return count

def main():
    a, b = map(int, input().split())

    is_prime = sosu(b)

    primes = [i for i, prime in enumerate(is_prime) if prime]

    count = 0
    for num in range(a, b + 1):
        factor_count = cut(num, primes)
        if factor_count > 0 and is_prime[factor_count]:
            count += 1

    print(count)

if __name__ == "__main__":
    main()