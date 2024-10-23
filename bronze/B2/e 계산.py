from math import factorial

print("n e")
print("- -----------")
e = 1
print(0, e)
for i in range(1, 10):
    e += 1 / factorial(i)
    if i == 1:
        print(i, 2)
    elif i == 2:
        print(i, 2.5)
    else:
        print("%d %.9f" % (i, e))