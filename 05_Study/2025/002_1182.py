'''
https://www.acmicpc.net/problem/1182
제목 : 부분수열의 합

문제)
- N개의 정수로 이루어진 수열
- 크기가 양수인 부분수열 중에서 그 수열의 원소를 다 더한 값이 S가 되는 경우의 수

입력)
5 0             - N : 정수의 개수, S : 합
-7 -3 -2 5 8    - N개의 정수

출력)
1              - 경우의 수
'''
import sys
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0

# 더하거나 안더하거나
def dfs(idx, sum):
    global cnt
    if idx == N:
        if sum == S:
            cnt += 1
        return
    dfs(idx + 1, sum + arr[idx])
    dfs(idx + 1, sum)

dfs(0, 0)

if S == 0: # S가 0일 경우, 공집합도 포함되므로 1을 빼준다
    cnt -= 1
print(cnt)

