import sys
input = sys.stdin.readline

x,y = map(int,input().split())
diff = y-x

if diff == 0:
    print(0)
elif diff == 1:
    print(1)
elif diff == 2:
    print(2)
else:
    for i in range(1,100000000):
        if i*(i+1) < diff <= i*(i+1)+(i+1):
            print(i*2+1)
            break
        if i*(i+1)+(i+1) < diff <= (i+1)*(i+2):
            print(i*2+2)
            break