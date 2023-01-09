'''
< N & M >
문제)
- N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성 하시오
    - N개의 자연수 중에서 M개를 고른 수열
입력)
- 1     : N, M ~ [1 \ 8]
- 2     : N개의 수가 주어진다.
출력)
- 1     : 조건에 만족하는 수열 출력 중복되는 수열 여러번 출력하면 안됨\
    사전순 출력
'''
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
visited = [0] * (n)
tmp = []

def dfs(x):
    global tmp, visited
    if x == m:
        print(*tmp)
        return
    prev = 0
    for i in range(n):
        if visited[n]: continue
        if nums[i] == prev: continue
        visited[i] = 1
        tmp.append(nums[i])
        prev = nums[i]
        dfs(x + 1)
        visited[i] = 0
        tmp.pop()

dfs(0)


    

