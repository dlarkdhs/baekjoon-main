import sys
input = sys.stdin.readline
import math

n = int(input())
k = 10
res = math.factorial(k+n-1)//(math.factorial(n)*math.factorial(k-1))
print(res%10007)