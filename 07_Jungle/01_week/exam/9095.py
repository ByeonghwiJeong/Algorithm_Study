'''
< 1, 2, 3 더하기 >
https://www.acmicpc.net/problem/9095
문제)
- 정수 4를 1 2 3합으로 나타내는 방법은 7가지가 있다.
(1,1,1,1)(1,1,2)(1,2,1)(2,1,1)(2,2)(1,3)(3,1)
'''
import sys
input = sys.stdin.readline

b = [1, 2, 3]

def dfs(s, n): # 첫번째 매개변수가 합, 두번째는 target
    global ret
    if n == s: # 합이 같으면
        ret += 1  # global로 선언한 전역변수 ret += 1
        return  # 
    if n < s: return # target보다 초과하면 OUT
    for i in b: # 
        dfs(s+i, n)
    return

for _ in range(int(input())):
    n = int(input())
    ret = 0
    dfs(0, n)
    print(ret)