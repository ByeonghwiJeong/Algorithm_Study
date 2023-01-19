'''
< A와 B2 >
https://www.acmicpc.net/problem/12919
문제)
- A와 B로만 이루어진 영어 단어 존재
- 두 문자열이 S와 T가 주어졌을 때,
    S >>>> T (S를 T로 바꾸는 게임)
    - 문자열의 뒤에 A를 추가
    - 문자열의 뒤에 B를 추가하고 문자열을 뒤집는다.
- S를 T로 만들 수 있는지 없는지?
    - Yes : 1
    - No  : 0
'''
import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

s = input().rstrip()
t = input().rstrip()
# 반대로 생각 T에서 S로 
def dfs(x):
    if x == s:
        print(1)
        sys.exit()
    if len(x) == len(s): return
    if x[-1] == 'A': dfs(x[:-1])
    if x[0] == 'B': dfs(x[1:][::-1])

dfs(t)
print(0)