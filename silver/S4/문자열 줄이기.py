import sys
from collections import Counter

input = sys.stdin.readline

# 입력 처리
n, m = map(int, input().split())
s = input().rstrip()

# 사전 순으로 가장 작은 문자 m개 구하기
char_count = Counter(s)
remove_list = sorted(char_count.elements())[:m]  # 가장 작은 문자 m개 선택

# 제거할 문자 빈도 계산
remove_count = Counter(remove_list)

# 결과 문자열 생성
result = []
for char in s:
    if remove_count[char] > 0:
        remove_count[char] -= 1  # 제거할 문자를 만나면 횟수 줄이기
    else:
        result.append(char)  # 남는 문자는 결과 리스트에 추가

# 출력
print(''.join(result))