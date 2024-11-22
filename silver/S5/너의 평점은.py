import sys
input = sys.stdin.readline


res = 0
res1 = 0
for _ in range(20):
    a,b,c = map(str,input().split())
    if c == 'A+':
        res1 += float(b)
        res += (float(b)*4.5)
    elif c == 'A0':
        res1 += float(b)
        res += (float(b)*4.0)
    elif c == 'B+':
        res1 += float(b)
        res += (float(b)*3.5)
    elif c == 'B0':
        res1 += float(b)
        res += (float(b)*3.0)
    elif c == 'C+':
        res1 += float(b)
        res += (float(b)*2.5)
    elif c == 'C0':
        res1 += float(b)
        res += (float(b)*2.0)
    elif c == 'D+':
        res1 += float(b)
        res += (float(b)*1.5)
    elif c == 'D0':
        res1 += float(b)
        res += (float(b)*1.0)
    elif c == 'F':
        res1 += float(b)
        pass
    elif c == 'P':
        pass
if res == 0.0 or res1 == 0.0:
    print("0.000000")
else:
    print(f'{res/res1}')