gold_rate = 1.618
dic = {}

m = int(input())
for _ in range(m):
    s, v = input().split()
    v = int(v)
    dic[s] = dic.get(s, 0) + v

flag = False
for val1 in dic.items():
    for val2 in dic.items():
        if int(val1[1] * gold_rate) == val2[1]:
            if val1[0] == val2[0]:
                continue
            flag = True
            break
    if flag:
        break

if flag:
    print("Delicious!")
else:
    print("Not Delicious...")