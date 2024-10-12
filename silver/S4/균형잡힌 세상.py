import sys
input = sys.stdin.readline

while True:
    n = input().rstrip()
    flag = 0
    check = []
    if n == '.':
        break
    for i in n:
        if i == '(' or i == '[':
            check.append(i)
        elif i == ')':
            if len(check) != 0 and check[-1] == '(':
                check.pop()
            else:
                flag = 1
                break
        elif i == ']':
            if len(check) != 0 and check[-1] == '[':
                check.pop()
            else:
                flag = 1
                break
    if len(check) == 0 and flag == 0:
        print('yes')
    else:
        print('no')