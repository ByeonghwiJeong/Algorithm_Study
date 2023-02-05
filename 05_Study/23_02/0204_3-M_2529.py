'''
< 부등호 >
https://www.acmicpc.net/problem/2529
문제)
- 두 종류의 부등호 기호 "<"와 ">"가 k개 나열된 순서열 A가 있다.
- 우리는 이 부등호 기호 앞뒤에 서로 다른 한 자릿수 숫자를 넣는다.
- 모든 부등호를 만족시킨다.
입력)
- 1     : 부등호 갯수 K ~ [2 \ 9]
- 2     : K개의 부등호들의 나열
출력)
- 1     : 최대 정수
- 2     : 최소 정수
'''

import sys
input = sys.stdin.readline

K = int(input())
a = input().split()
visited = [0] * 10
ret = []

def check(x, y, op):
    if x < y and op == "<": return True
    if x > y and op == ">": return True
    return False

def bfs(x, nums):
    global ret
    if x == K + 1:
        ret.append(nums)
        return
    for i in range(10):
        if visited[i]: continue
        if x == 0 or check(int(nums[x - 1]), i, a[x - 1]):
            visited[i] = 1
            bfs(x + 1, nums + str(i))
            visited[i] = 0
    return

bfs(0, "")
ret.sort()
print(ret[-1])
print(ret[0])

'''
값 비교를 못하는 index 0인경우 백트래킹 진행 조건문
if(x == 0 or 원래조건체크)
'''