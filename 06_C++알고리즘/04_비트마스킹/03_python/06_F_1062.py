'''
https://www.acmicpc.net/problem/1062
제목 : 가르침

문제 
- 26개의 알파벳 중에서 K개의 글자만 배울 수 있다.
- K개의 글자로만 이루어진 단어만 읽을 수 있다.
- 어떤 K개의 글자를 배웠을 때, 읽을 수 있는 단어의 개수의 최댓값을 구하라.
- 모든단어는 "anta"로 시작하고, "tica"로 끝난다.
- N개의 단어가 주어진다.
- 비트마스킹 활용
'''
import sys
from itertools import combinations
input = sys.stdin.readline

def word_to_bit(word):
    result = 0
    for w in word:
        result |= (1 << (ord(w) - ord('a'))) # `n |= (1 << x)` : x번째 비트 ON
    return result

N, K = map(int, input().split())
words = [input().rstrip() for _ in range(N)]
bits = list(map(word_to_bit, words)) # 단어를 비트로 변환
base_bit = word_to_bit('antatica')

if K < 5:
    print(0)
    exit()
else:
    alphabet = [1 << i for i in range(26) if not (base_bit & (1 << i))]
    # `if(n & (1 << x))` : check ~ x번째 비트 확인
    ans = 0
    for comb in combinations(alphabet, K-5): # 5개는 이미 배웠으므로 5개를 뺀다.
        temp = base_bit # 5개를 미리 배워놓는다.
        for c in comb: # 5개를 제외한 나머지를 추가한다.
            temp |= c
        cnt = 0 # 단어의 개수
        for bit in bits: # 단어를 비교한다.
            if bit & temp == bit: # 단어를 읽을 수 있는 경우
                cnt += 1
        ans = max(ans, cnt)
    print(ans)


'''
⭐⭐⭐`비트 마스킹`⭐⭐⭐
공집합에 x를 추가
=> x번째에 1을 or연산자로 추가 
=> n의 범위가 최대 20 (n이 30이하이므로 비트마스킹 적용가능)
### `add` : x번째 비트 ON
- `n |= (1 << x)`
- OR연산자는 이미 있는경우는 무시

### `remove` : x번째 비트 OFF
- `n &= ~(1 << x)`

### `check` : x번째 비트 확인
- `if(n & (1 << x))`
- python 삼항 연산자
    - 참인경우 if 조건 else 거짓인경우

### `toggle` : x번째 비트 XOR연산
- 0은 1, 1은 0
    - x가 있으면 x를 제거, 없으면 x를 추가
- `n ^= (1 << x)`

### `all` : 크기가 21인 집합의 모든 비트를 켜기
- 1 ~ 20 표현하기위해서 크기 21
- `(1 << 21) - 1`

###  `empty` : 공집합으로 만들기
- n = 0
'''