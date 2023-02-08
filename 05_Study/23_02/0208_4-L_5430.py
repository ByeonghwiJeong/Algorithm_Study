'''
< AC >
https://www.acmicpc.net/problem/5430
문제)
- 새로운 언어 AC 만듬
    - 정수 배열에 연산을 하기 위한 언어
- 두가기 함수 R, D 존재
    - 함수 R (뒤집기)
        - 배열에 있는 수의 순서를 뒤집기
    - 함수 D
        - 첫 번째 수를 버리는 함수
        - 배열이 비어있는경우 에러 발생
입력)
- 1     : 테스트 케이스 T
- 2     : 수행할 함수 p
- 3     : 배열에 들어있는 수의 개수 n
- 4     : 배열
출력)
- 함수를 실행한 결과 or 에러 발생 "error"
'''
import sys
from collections import deque
input = sys.stdin.readline

def oper(k):
    global dq, direction
    if k == 'R': direction = not direction
    elif k == 'D':
        if x:
            if direction: x.popleft()
            else: x.pop()
        else: return False
    return True        

for _ in range(int(input())):
    p = input().rstrip()
    n = int(input())
    a = input().rstrip()[1:-1]

    if a: x = deque(a.split(','))
    else: x = deque()

    direction = True

    for o in p:
        if not oper(o):
            print('error')
            break
    else:
        if not direction:
            x.reverse()
        print('[', end='')
        print(*x, sep=',', end=']\n')

'''
1. string 배열을 진짜 배열로 만들기
    - 예외case: '[]'
2. 직접 뒤집으면 안된다 - 시간초과 방지
    - 방향 boolean상수 `direction`선언
'''