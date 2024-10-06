import sys
input = sys.stdin.readline

x = input()
if '-x' in x:
    x = x.replace('-x','-1x')
if 'x' in x:
    if x[0] == 'x':
        print(1)
    else:
        li = list(map(str,x.split('x')))
        print(li[0])
else:
    print(0)