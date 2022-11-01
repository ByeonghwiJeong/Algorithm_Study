'''
입력
5 : 갯수
-1 0 0 1 1 : 0번~N-1번노드의 부모번호
2 : 삭제할 노드의 번호
< 다른 풀이 2 > 
1. 입력된 인덱스삭제하기 위해 dfs함수에 트리 배열과 함께 전달
2. dfs함수
    2-1. 전달받은 인덱스의 배열 값을 삭제한다는 의미로 -2로 바꾼다.
    2-2. 배열 전체를 탐색하며, 방금 삭제한 인덱스를 부모노드로 가지는 노드를 찾아 dfs재귀함수호출
3. 재귀가 끝나면 삭제될노드들은 전부 -2로 갱신
4. -2가 아니면서 다른노드의 부모노드가 아닌경우

'''
import sys
input = sys.stdin.readline

n = int(input())
tree = list(map(int, input().split()))
d = int(input())

def dfs(r, tree):
    tree[r] = -2
    for i in range(n):
        if tree[i] == r:
            dfs(i, tree)

dfs(d, tree) # 삭제할 노드 전달
count = 0
for i in range(n):
    if tree[i]!=-2 and i not in tree:
        count += 1
print(count)


dfs(tree=tree, r=d)