R, C = map(int, input().rstrip().split())

arr = []

for i in range(R):
    string = input()
    arr.append(list(string))
    
x, y = map(int, input().rstrip().split())

for i in range(R):
    for j in range(C, 2*C):
        arr[i].append(arr[i][2*C-1-j])

for i in range(R, 2*R):
    arr.append([])
    for j in range(C):
        arr[i].append(arr[2*R-1-i][j])
    
for i in range(R, 2*R):
    for j in range(C, 2*C):
        arr[i].append(arr[2*R-1-i][2*C-1-j])

if arr[x-1][y-1] == '.':
    arr[x-1][y-1] = '#'
elif arr[x-1][y-1] == '#':
    arr[x-1][y-1] = '.'

for i in range(2*R):
    for j in range(2*C):
        print(arr[i][j], end = "")
    print()