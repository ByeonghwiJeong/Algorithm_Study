'''
암로를 만든다.
서로 다른 L개의 알파벳 소문자들로 구성
최소 한 개의 모음(a, e, i, o, u)과 최소 두 개의 자음으로 구성
입력)
- 암호는 L개의 알파벳 소문자들로 구성, C개의 문자
출력)
- 각줄에 하나씩 사전식 출력
'''
import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

L, C = map(int, input().split())
_list = input().rstrip().split(' ')
_list.sort()
col = ["a", "e", "i", "o", "u"]
visited = [0] * C

def dfs(l, n, num): # l길이, n모음수, num암호길이
    global visited
    if num == L:
        if n >= 1 and num - n >= 2:
            for i in range(C):
                if visited[i]:
                    print(_list[i], end='')
            print()
        return
    if l == C: # 위치때문에 정답찾는데 시간걸림
        return
    else:
        # 선택 O
        visited[l] = 1
        if _list[l] in col: # 모음이면 선택
            dfs(l + 1, n + 1, num + 1)
        else: # 그냥 선택
            dfs(l + 1, n, num + 1)
        visited[l] = 0
        # 선택 X
        dfs(l + 1, n, num)


dfs(0, 0, 0)

'''
if l == C를 print위에 위치시켜서 출력이 이상하게나왔다
'''