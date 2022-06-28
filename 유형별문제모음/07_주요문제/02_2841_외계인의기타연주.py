'''
손가락 수억개
기타는 1~6번줄
각줄은 P개의 프렛으로 나누어짐
- 프렛 번호 1번 ~ P번
예) 8번 프렛을 누르고 4번줄을 튕길 수 있다.
프렛을 여러개 누르고 있다면 가장 높은 프렛 적용
예)
 1. 3번줄_on 5번P_on
 2. 7번P 연주시 : 5번_off할 필요없음
    5번P & 7번P 동시 on
 3. 2번P 연주시 : 5번P & 7번P 동시 off

문제) 손가락 가장 적게 움직이는 수 출력
음의 수 N, 한줄에 있는 프렛의 수 P
N < 500,000  2 =< P =< 300,000

입력) 
N P
줄번호 프렛번호 * N번

[[ 스택 자료구조로 구현!!! ]]
'''

import sys
input = sys.stdin.readline

N, P = map(int, input().split())
stk = [[] for  _ in range(7)] # 6개줄 각각의 stack
ans = 0
for _ in range(N):
    line, p = map(int, input().split())
# 스택 구현시 내부의 값이 있는지 없는지 확인 if stk:
    while stk[line] and stk[line][-1] > p:
        stk[line].pop()
        ans +=1
    if stk[line] and stk[line][-1] == p:
        continue
    stk[line].append(p)
    ans += 1
print(ans)