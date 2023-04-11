'''
< 줄서기 >
https://www.acmicpc.net/problem/14864
문제)
- N명의 학생들이 앞뒤로 일려로 서있다.
- 1부터 N까지의 번호가 붙어있다.
- 학생들은 자신보다 뒤에 서 있고 더 작은 번호의 학생명단을 받았다.
- (X, Y) : 학생Y가 학생X보다 뒤에 있으면서 작은 번호를 가지고 있다.

'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
visited = [0] * (N+1)
v = [0] * (N+1)
flag = 0

for i in range(M):
    X, Y = map(int, input().split())
    # 학생X는 학생Y보다 앞에 있으면서 큰번호를 가지고 있다.
    v[X] += 1
    v[Y] -= 1

for i in range(1, N+1):
    v[i] += i
    visited[v[i]] += 1

for i in range(1, N+1):
    if visited[i] == 0 or visited[i] > 2:
        flag = 1
        break
    
if flag: print(-1)
else: print(*v[1:])