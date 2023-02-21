'''
< 자두나무 >
https://www.acmicpc.net/problem/2240
문제)
- 키가 작은 자두를 먹지는 못한다.
- 떨어질 째까지 기다린 다음에 떨어지는 자두를 받아서 먹는다.
- 자두를 잡을때에는 자두가 허공에 있을 때 잡아야한다.
- 매초마다 두개의 나무중 하나의 나무에서 열매가 떨어진다.
- 열매가 떨어지는 순간 그 나무 아래에 서있으면 그 열매를 먹을수 있다.
- 두 개의 나무는 가까이에 있어서 다른나무로 빠르게이동가능하다.
- 자두는 T초 ~ [1 \ 1,000] 동안 떨어진다.
- 자두는 최대 W ~ [1 \ 30] 번만 움직이고 싶어한다.
- 매초마다 어느 나무에서 자두가 떨어질지에 대한 정보가 있을 때
- 받을 수 있는 자두의 개수
'''
import sys

def go(idx, tree, cnt):
    # 기저사례
    if cnt < 0: return -1
    if idx == T: return 0
    # 메모이제이션 & 초기화
    if dp[idx][tree][cnt] != -1: return dp[idx][tree][cnt]
    ret = max(go(idx + 1, tree ^ 1, cnt - 1), go(idx + 1, tree, cnt))
    if tree == a[idx] - 1: ret += 1
    dp[idx][tree][cnt] = ret
    return ret

T, W = map(int, input().split())
a = [int(input()) for _ in range(T)]
# 초기화
dp = [[[-1 for _ in range(W+2)] for _ in range(2)] for _ in range(T+2)]
print(max(go(0, 1, W - 1), go(0, 0, W)))

'''
중요한 상태값
- 1000초
- W : 최대이동횟수
- idx : 첫번째 or 두번째

기저사례
메모이제이션
로직
초기화
'''

