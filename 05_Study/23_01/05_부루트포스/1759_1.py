import sys
from itertools import combinations
input = sys.stdin.readline

vowels = ['a', 'e', 'i', 'o', 'u']

def is_valid(cypher):
    count = 0 # 모음의 수
    for i in cypher:
        if i in vowels:
            count += 1

    # 모음 자음 조건
    return count >= 1 and len(cypher) - count >= 2

# 입력
n, m = map(int, input().split())
alphabets = list(input().split())

alphabets.sort()

for cypher in combinations(alphabets, n):
    if is_valid(cypher): # 유효한 암호일 경우
        print(''.join(cypher))