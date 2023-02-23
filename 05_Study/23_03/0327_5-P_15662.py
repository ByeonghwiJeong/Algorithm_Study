'''
< 톱니바퀴2 > 
https://www.acmicpc.net/problem/15662
문제)
- 8개의 톱니를 가지고 있는 톱니바퀴 T개가 일렬
    - 1번~T번
- N극 또는 S극 중 하나를 나타내고 있다.
- 회전시킬 톱니바퀴와 회전방향을 결정해야함
- 극에 따라서 옆에있는 톱니바퀴를
입력)
- 1     : 톱니바퀴의 개수 T ~ [1 \ 1000]
- 2[T]  : 톱니바퀴의 상태(8개의정수) : N~
    - N극:0, S극:1
    - 12시방향부터 시계방향순서
- 3     : 회전횟수K ~ [1 \ 1000]
- 4[K]  : 회전시킨 톱니번호, 방향
    - 시계방향1, 반시계방향-1
출력)
- 1     : K번 회전시킨 이후에 12시방향이 S극인 톱니바퀴의 개수
'''
import sys

N = int(input())
S = [input().rstrip() for _ in range(N)]
K = int(input())

def rot(pos, dir):
    global S
    if dir: # 반시계방향 1
        S[pos] = S[pos][-1] + S[pos][:-1]
    else: # 시계 0
        S[pos] = S[pos][1:] + S[pos][0]

def findL(pos): # 왼쪽 어디까지 회전?
    for i in range(pos, 0, -1):
        if S[i][6] == S[i - 1][2]: return i
    return 0

def findR(pos): # 오른쪽 어디까지 회전?
    for i in range(pos, N - 1):
        if S[i][2] == S[i + 1][6]: return i
    return N - 1

for _ in range(K):
    a, b = map(int, input().split())
    a -= 1 # index기준으로 0부터
    b = 0 if b == -1 else 1
    l = findL(a)
    r = findR(a)
    cnt = 0 # 방향성 체크
    for pos in range(a, l - 1, -1):
        rot(pos, b if cnt % 2 == 0 else not b)
        cnt += 1
    cnt = 1
    for pos in range(a + 1, r + 1):
        rot(pos, b if cnt % 2 == 0 else not b)
        cnt += 1

ret = sum(1 for i in range(N) if S[i][0] == '1')
print(ret)

'''
반대 방향성을 표현할때는 주어진 조건이 0과 1이 아닌경우에도
0과 1로 바꾸어주는것이 not으로 반대로 만들 수 있어서 편하다
'''
