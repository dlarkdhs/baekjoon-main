import sys
imput = sys.stdin.readline

arr = input().strip() + " "
stack = []
res = ''

flag = 0
for i in arr:
    if i == "<":
        flag = 1
        for _ in range(len(stack)):
            res += stack.pop()
    stack.append(i)
    
    if i == ">":
        flag = 0
        for _ in range(len(stack)):
            res += stack.pop(0)
    
    if i == " " and flag == 0:
        stack.pop()
        for _ in range(len(stack)):
            res += stack.pop()
        res += " "
print(res)