import sys
input = sys.stdin.readline

a,b = input().split()
leng = abs(len(a)-len(b))

if len(a) < len(b):
    a = ('0'*leng)+a
elif len(a) > len(b):
    b = ('0'*leng)+b
res = ''
for i in range(len(a)):
    res += str(int(a[i])+int(b[i]))
print(res)