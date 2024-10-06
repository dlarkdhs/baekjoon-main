import sys
input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n):
    input_line = input().split()
    command = input_line[0]

    if command == "push":
        stack.append(int(input_line[1]))
    elif command == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif command == "size":
        print(len(stack))
    elif command == "empty":
        print(0 if stack else 1)
    elif command == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)