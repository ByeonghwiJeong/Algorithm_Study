'''
두 가지 함수
R : 뒤집기
D : 버리기(첫번째)
    - 빈배열 인경우 error
'''
from collections import deque
import sys
input = sys.stdin.readline

# def operate(o):
#     global x
#     if o == 'R':
#         x.reverse()
#     elif o == 'D':
#         if x:
#             x.popleft()
#         else:
#             return False
#     return True

def operate(o):
    global x, direction
    if o == 'R':
        if direction:
            direction = False
        else:
            direction = True
    elif o == 'D':
        if x:
            if direction:
                x.popleft()
            else:
                x.pop()
        else:
            return False
    return True
        

for _ in range(int(input())):
    p = input().rstrip()
    n = int(input())
    # _nums = list(map(int, input().rstrip().strip('][').split(',')))
    _nums = input().rstrip()[1:-1]

    if _nums:
        x = deque(_nums.split(','))
    else:
        x = deque()

    direction = True

    for o in p:
        if not operate(o):
            print('error')
            break
    else:
        if not direction:
            x.reverse()
        print('[' + ','.join(x) + ']')
'''
입력 방식 주의!!!!
[1,2,3,4]
빈배열 []도 처리해야함!!!

시간초과 발생
>>> R나올때 마다 reverse 하면 시간초과 발생
>>> flag를 설정해서 마지막에 반환
'''