import sys
input = sys.stdin.readline

ans = 0
for j in [3,2,1]:
    i = input().rstrip()
    if i not in ['Fizz','Buzz','FizzBuzz']:
        ans = int(i)+j
if ans % 3 == 0 and ans % 5 == 0:
    print('FizzBuzz')
elif ans % 3 == 0:
    print('Fizz')
elif ans % 5 == 0:
    print('Buzz')
else:
    print(ans)