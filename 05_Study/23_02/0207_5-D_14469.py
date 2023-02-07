'''
< 소가 길을 건너간 이유 3 >
https://www.acmicpc.net/problem/14469
문제)
- N마리 소가 농장에 방문
- 소가 도착한 시간과 검문시간은 소마다 다르다.
- 모든 소가 농장 입장시 걸리는 시간
입력)
- 1     : 100이하 양의 정수N
- 2[N]  : 도착시간, 검문시간
'''
import sys
input = sys.stdin.readline

N = int(input())
a = [tuple(map(int, input().split())) for _ in range(N)]
# a.sort(key=lambda x : x[0])
a.sort()
ret = a[0][0] + a[0][1]
for i in range(1, N):
    ret = max(ret, a[i][0])
    ret += a[i][1]
print(ret)