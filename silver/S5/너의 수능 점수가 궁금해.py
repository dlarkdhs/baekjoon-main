POSTAL_CODE = 4763
BUILDING_KR_ENG_HIGH = 508
BUILDING_KR_ENG_LOW = 108
BUILDING_MATH_SCI_HIGH = 212
BUILDING_MATH_SCI_LOW = 305


def find_possible_scores(S):
    if S % POSTAL_CODE != 0:
        return []
    target_sum = S // POSTAL_CODE

    results = []

    for kr_eng_diff in range(201):
        for math_sci_diff in range(201):
            A1 = kr_eng_diff * BUILDING_KR_ENG_HIGH
            A2 = kr_eng_diff * BUILDING_KR_ENG_LOW
            B1 = math_sci_diff * BUILDING_MATH_SCI_HIGH
            B2 = math_sci_diff * BUILDING_MATH_SCI_LOW

            if A1 + B1 == target_sum or A1 + B2 == target_sum or \
               A2 + B1 == target_sum or A2 + B2 == target_sum:
                results.append((kr_eng_diff, math_sci_diff))

    results.sort(key=lambda x: (x[0], x[1]))
    return results


S = int(input())
possible_scores = find_possible_scores(S)

if not possible_scores:
    print(0)
else:
    print(len(possible_scores))
    for kr_eng_diff, math_sci_diff in possible_scores:
        print(kr_eng_diff, math_sci_diff)
