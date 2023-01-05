'''
< 숫자 야구 >
문제)
- 영수 : 1 ~ 9 서로다른 숫자 세 자리 수를 마음속으로 생각
- 민혁 : 1 ~ 9 서로다른 숫자 세 자리 수를 마음속으로 생각
- 세 자리 수 중하나가 세 자리 수의 동일한 자리에 위치하면 스트라이크 한번
- 세 자리 수 중하나가 세 자리 수의 다른 자리에 위치하면 볼 한번
- ㅅ
- 예)
    - 영수 324
    - 429 : 1S1B
    - 241 : 0S2B
    - 924 : 2S0B
- 정확히 3자리수 맞추어 3스트라이크가 되면 게임이 끝난다.
입력)
- 1     : 몇번 질문 했는지?
- 2     : 세자리수, S, B
출력)
- 가능성이 있는 답의 총 개수
'''
from itertools import permutations
import sys
input = sys.stdin.readline

n = int(input())
init_input = lambda x: (x[0], (int(x[1]), int(x[2])))
questions = [init_input(input().split()) for _ in range(n)]

def count_strike_ball(s1, s2):
    # a가 답이라고 가정, b에 대한 스트라이크와 볼 수를 세서 리턴
    strike = 0
    ball = 0
    for i in range(3):
        if s2[i] == s1[i]: # 위치 숫자 모두 OK
            strike += 1
        elif s2[i] in s1:
            ball += 1
    return (strike, ball)

def count_answer():
    digits = [str(i) for i in range(1, 10)]
    numbers = set(permutations(digits, 3))

    for s1, count in questions:
        tmp = set()
        for s2 in numbers:
            if count_strike_ball(s1, s2) == count:
                tmp.add(s2)
        numbers = tmp
    return len(numbers)

print(count_answer())