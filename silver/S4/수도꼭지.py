import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
A = a[:]
q = int(input())

# 초깃값 설정
res = [sum(a)]
a1 = [1] * n
current_sum = res[0]

for _ in range(q):
    sen = list(map(int, input().split()))
    if sen[0] == 2:
        index = sen[1] - 1
        if a1[index] == 1:
            current_sum -= A[index]
            a1[index] *= -1
        else:
            current_sum += A[index]
            a1[index] *= -1
        res.append(current_sum)
    else:
        index = sen[1] - 1
        new_value = sen[2]
        if a1[index] == 1:
            current_sum += new_value - A[index]
        A[index] = new_value
        res.append(current_sum)

for value in res:
    print(value)
