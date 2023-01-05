'''
< 암호 만들기 >
- 서로 다른 L개의 알파벳 소문자
    - 최소 한개의 모음(a, e, i, o, u)
    - 최소 두 개의 자음
- 정렬된 문자열을 선호
    - 알파벳이 암호에서 증가하는 순서로 배열
입력)
- 1     : 암호길이L, 주어진문자수C
- 2     : 문자C
'''
L, C = map(int, input().split())
l = input().split()
visited = [0] * (C + 1)
l.sort()
check = {'a', 'e', 'i', 'o', 'u'}

# a 모음수, b 자음수
def dfs(idx, a, b):
    if idx == C:
        if a + b == L:
            if a >= 1 and b >= 2:
                for i in range(C):
                    if visited[i]:
                        print(l[i], end='')
                print()
        return
    visited[idx] = 1
    if l[idx] in check: dfs(idx + 1, a + 1, b) # 모음선택
    else: dfs(idx + 1, a, b + 1) # 자음선택
    visited[idx] = 0
    dfs(idx + 1, a, b) # 선택 X

  
dfs(0, 0, 0)