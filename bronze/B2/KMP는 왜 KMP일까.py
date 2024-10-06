import sys
input = sys.stdin.readline

short_name = []
name = input()
short_name.append(name[0])
for i in range(len(name)):
    if name[i] == '-':
        short_name.append(name[i+1])
print(*short_name, sep = '')