# import sys
# input = sys.stdin.readline

# 3번.
# numbers=[1,2,3,4]
# print(numbers[2])
# 3

# 14번.
# for i in range(3):
#     print(i)
# 0 /n 1 /n 2

# 21번.
# if 5>3: print('참')
# else: print('거짓')
# 참

# 24번.
# nums = [10,20,30]
# nums.append(40)
# print(nums)
# [10, 20, 30, 40]

# 25번.
# lst=[1,2,3,4,5]
# print(lst[1:4])
# [2, 3, 4]

# 36번.
# for i in range(5):
#     if i == 3:
#         continue
#     print(i)
# 0, 1, 2, 4

# 40번.
# def add(a, b):
#     return a + b
# print(add(2, 3))
# 5

# 41번.
# def subtract(a, b):
#     return a - b
# result = subtract(b=10, a=20)
# print(result)
# 10

# 43번.
# def repeat(word, times):
#     return word * times
# print(repeat("Hi", 3))
# HiHiHi

# 44번.
# def print_name(name="John"):
#     print(name)
# print_name("Alice")
# Alice

# 45번.
# def calc_square(x):
#     return x ** 2
# print(calc_square(4))
# 16

# <손코딩 문제(부분 코딩 또는 풀코딩)>
# 1.
# while True:
#     n = int(input("정수를 입력하시오>> "))
#     if n == 0:
#         break
#     if n % 2 == 0:
#         print(f'입력한 정수 {n}은 짝수입니다.')
#     else:
#         print(f'입력한 정수 {n}은 홀수입니다.')

# 2.
# n = int(input("30보다 작은 정수를 입력하시오>> "))
# if n >= 30:
#     print("범위를 벗어난 수를 입력했습니다.")
# else:
#     for i in range(n,31):
#         print(i)

# 3.
# n = int(input())
# if n == 0:
#     print("범위를 벗어남")
# else:
#     s = 0
#     for i in range(1,n+1):
#         if i % 2 == 0:
#             s += i
#     print(s)

# 4.
# s = 0
# for i in range(50,101):
#     if i % 3 == 0 or i % 5 == 0:
#         s += i
# print(s)

# 5.
# while True:
#     ans = int(input("87+36 = ?"))
#     if ans != 123:
#         print("X")
#     else:
#         print("Correct")
#         break

# 8.
# def even_odd(n):
#     if n % 2 == 0:
#         print(f'{n} = 짝수')
#     else:
#         print(f'{n} = 홀수')
# a = int(input())
# if a == 0:
#     print("입력한 수는 0입니다.")
# else:
#     even_odd(a)

# 10.
# def CeltoFar(temp):
#     return ((9/5)*temp+32)
# c = float(input("섭씨온도를 입력하시오>> "))
# print(CeltoFar(c))

# 11.
# def change_meter(meter):
#     feet = meter / 0.305
#     yard = meter * 1.0936
#     return (feet,yard)
# m = float(input())
# f,y = change_meter(m)
# print(f'{m} = {f:.3f}ft')
# print(f'{m} = {y:.3f}yd')