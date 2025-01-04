"""
https://www.acmicpc.net/problem/4659
제목: 비밀번호 발음하기

"""

import sys
input = sys.stdin.readline

def is_vowel(c):
    return c in 'aeiou'


"""
1. 모음(a, e, i, o, u) 하나를 반드시 포함
2. 모음이 3개 혹은 자음이 3개 연속으로 오면 안됨
3. 같은 글자 연속 2번 안됨 (ee, oo 제외 - 허용)
"""
def is_valid(word):
    has_vowel = False # 조건(1)
    vowel_cnt = 0     # 연속 모음수
    consonant_cnt = 0 # 연속 자음수
    prev = None       # 이전 글자

    for c in word:
        # 조건(1)
        if is_vowel(c):
            has_vowel = True
            consonant_cnt = 0
            vowel_cnt += 1
        else:
            vowel_cnt = 0
            consonant_cnt += 1

        # 조건(2) 
        if vowel_cnt == 3 or consonant_cnt == 3:
            return False
        
        # 조건(3)
        if c == prev and c not in 'eo':
            return False
        
        prev = c

    # 조건(1)
    return has_vowel

while (word := input().strip()) != 'end':
    if is_valid(word):
        print(f"<{word}> is acceptable.")
    else:
        print(f"<{word}> is not acceptable.")