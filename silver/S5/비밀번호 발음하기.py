import sys
input = sys.stdin.readline

while True:
    a = input().strip()
    if a == 'end':
        break

    moeum = {'a', 'e', 'i', 'o', 'u'}
    
    has_vowel = any(char in moeum for char in a)
    if not has_vowel:
        print(f"<{a}> is not acceptable.")
        continue

    is_acceptable = True
    for i in range(len(a) - 2):
        if (a[i] in moeum and a[i+1] in moeum and a[i+2] in moeum) or \
           (a[i] not in moeum and a[i+1] not in moeum and a[i+2] not in moeum):
            is_acceptable = False
            break

    if is_acceptable:
        for i in range(len(a) - 1):
            if a[i] == a[i+1] and a[i] not in {'e', 'o'}:
                is_acceptable = False
                break

    if is_acceptable:
        print(f"<{a}> is acceptable.")
    else:
        print(f"<{a}> is not acceptable.")
