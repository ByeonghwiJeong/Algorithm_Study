'''
< 2048 (Easy) >
https://www.acmicpc.net/problem/12100
문제)
- N x N
- 최대 5번 이동해서 만들 수 있는 가장 큰 블록의 값을 구하라
입력)
- 1     : N ~ [1 \ 20]
- 2[NxN]: 
'''

import sys
from copy import deepcopy

N = int(input())
a = [list(map(int, input().split())) for _ in range(N)]

# 90도 회전
def rotate(B):
    tmp = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            tmp[i][j] = B[N - 1 - j][i]
    return tmp
# 일차원 list에 같은값이 있으면 왼쪽으로 이동시켜서 합침
def convert(B):
    tmp = [i for i in B if i != 0] # 0을 제외한 list저장
    for i in range(1, len(tmp)):
        if tmp[i - 1] == tmp[i]:
            tmp[i - 1] *= 2
            tmp[i] = 0
    tmp = [i for i in tmp if i != 0]
    return tmp + [0] * (N - len(tmp))
#
ret = 0 
def dfs(B, cnt):
    global ret
    if cnt == 5:
        ret = max(ret, max([max(i) for i in B]))
        return 
    for _ in range(4):
        C = [convert(i) for i in B]
        dfs(C, cnt + 1)
        B = rotate(B)
    return 

dfs(a, 0)
print(ret)
# def dfs(B, cnt):
#     ret = max([max(i) for i in B])
#     if cnt == 5:
#         return ret
#     for _ in range(4):
#         C = [convert(i) for i in B]
#         ret = max(ret, dfs(C, cnt + 1))
#         B = rotate(B)
#     return ret

# print(dfs(a, 0))

'''
### 4방향의 로직구현이 XX
- 1. 1방향로직
    - 일차원 배열에서 같은것 합치기 왼쪽으로 밀기
- 2. 90도 rotate (암기)
```python
# 90도 회전
def rotate(B):
    tmp = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            tmp[i][j] = B[N - 1 - j][i]
    return tmp
```
'''