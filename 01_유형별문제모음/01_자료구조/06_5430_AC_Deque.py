'''
함수 R
    - 배열에 있는 순의 순서를 뒤집기
함수 D
    - 첫 번째 수를 버리는 함수

입력)
    - 첫째 줄 : 테스트 케이스의 개수 T (T<=100)
    < Test Case > p + n ≤ 700,000
    - Test 1: 수행할 함수 p
    - Test 2: 배열에 들어있는 수의 개수 n
    - Test 3: [x1,...,xn]  (1 ≤ xi ≤ 100)
출력)
    - 테스트 케이스에 대하여, 수행한 결과를 출력
'''
from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    p = input().rstrip()
    n = int(input())
    chk = input().rstrip()[1:-1] 
    # 여기서 [] check
    if chk:
        chk = chk.split(',') 
        # 이런식으로 하는것이 최선인가?
    dq = deque(chk)
    direction = True
    for s in p:
        if s == 'R':
            if direction:
                direction = False
            else:
                direction = True
        elif s == 'D':
            if len(dq) < 1:
                print('error')
                break
            if direction:
                dq.popleft()
            else:
                dq.pop()
    else:
        if not direction:
            dq.reverse()
        print('[' + ','.join(dq) + ']')
