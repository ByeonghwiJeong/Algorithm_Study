'''
이진트리(깊이 우선 탐색)
1
2 3
45|67
전위 순회 1 2 4 5 3 6 7
중위 순회 4 2 5 1 6 3 7
후위 순회 4 5 2 6 7 3 1
'''
def dfs1(v): # 전위 순회 - 보통 문제풀이방식
    if v > 7:
        return
    print(v, end=' ')
    dfs1(v*2)
    dfs1(v*2+1)

def dfs2(v): # 후위 순회
    if v > 7:
        return
    dfs2(v*2)
    dfs2(v*2+1)
    print(v, end=' ')

def dfs3(v): # 중위 순회
    if v > 7:
        return
    dfs3(v*2)
    print(v, end=' ')
    dfs3(v*2+1)

dfs1(1)
print()
dfs2(1)
print()
dfs3(1)