'''
다음과 같이 여러 단위의 동전이 주어졌을때
거스름돈을 가장 적은 수의 동전으로 교환 해주려면
각 단위의 동전은 무한정 쓸 수 있다.

입력)
첫 번째 줄에는 동전의 종류개수 N(1<=N<=12)
두 번째 줄에는 N개의 동전의 종류
다음줄에 거슬러 줄 금액 M(1<=M<=500)
'''
import sys
sys.setrecursionlimit(10 ** 7)
from collections import deque


N = int(input())
nums = list(map(int, input().split()))
nums.sort()
M = int(input())
result = 1000000
result2 = 0

def dfs(L, sum):
    global result
    if L >= result:
        return
    if sum > M:
        return
    if sum == M:
        if L < result:
            result = L
    else:
        for i in range(N):
            dfs(L+1, sum+nums[i])

dfs(0, 0)
print(result)

def bfs():
    q = deque()
    for i in nums:
        q.append((i, 1))
    while q:
        sum2, cnt = q.popleft()
        if sum2 > M:
            continue
        if sum2 == M:
            print(cnt)
            return
        cnt += 1
        for i in nums:
            x = sum2 + i
            q.append((x, cnt))
bfs()

'''
같은 문제를 bfs와 dfs로 풀어봤다
핵심은 합이 특정값과 일치한경우이므로
dfs 매개변수와 bfs의 queue안에
합과 길이를 넣어줬다 
'''