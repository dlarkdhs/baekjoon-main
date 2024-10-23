num = list(map(int, input()))
n = 1  

while len(num) >= n:
    if len(num) > n and num[-n] > 4:
        num[-n-1] += 1  
        num[-n] = 0  
    elif len(num) > n and num[-n] <= 4:  
        num[-n] = 0 
    n += 1  

print(*num, sep='')