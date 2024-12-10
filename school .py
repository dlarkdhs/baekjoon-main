import sys
input = sys.stdin.readline

# 3번.
numbers=[1,2,3,4]
print(numbers[2])
# 3

# 14번.
for i in range(3):
    print(i)
# 0 /n 1 /n 2

# 21번.
if 5>3: print('참')
else: print('거짓')
# 참

# 24번.
nums = [10,20,30]
nums.append(40)
print(nums)
# [10, 20, 30, 40]

# 25번.
lst=[1,2,3,4,5]
print(lst[1:4])
# [2, 3, 4]

# 36번.
for i in range(5):
    if i == 3:
        continue
    print(i)
# 0, 1, 2, 4

# 40번.
def add(a, b):
    return a + b
print(add(2, 3))
# 5

# 41번.
def subtract(a, b):
    return a - b
result = subtract(b=10, a=20)
print(result)
# 10

# 43번.
def repeat(word, times):
    return word * times
print(repeat("Hi", 3))
# HiHiHi

# 44번.
def print_name(name="John"):
    print(name)
print_name("Alice")
# Alice

# 45번.
def calc_square(x):
    return x ** 2
print(calc_square(4))
# 16

# <손코딩 문제(부분 코딩 또는 풀코딩)>
# 1. 변수 s1에 "대한", s2에 "민국" 문자열을
# 대입한 후, 다음 형태로 출력해보자.

s1 = "대한"
s2 = "민국"
print(s1+s2)
print(s1,s2)
print(s1+s2,"만세")