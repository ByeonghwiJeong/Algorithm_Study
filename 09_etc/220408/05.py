"""
< Minimum Tree Path >

root node : 1 에서 시작
- 아래로 내려가면서 visitNodes에 있는 노드를 방문하고 
"""

from collections import deque


def minimumTreePath(n, edges, visitNodes):
    # Write your code here
    trees = [[] for _ in range(n + 1)]
    for edge in edges:
        trees[edge[0]].append(edge[1])
        trees[edge[1]].append(edge[0])
    for tree in trees:
        tree.sort()
    visited = [0] * (n + 1)
    dq = deque()
    dq.append(1)
    visited[1] = 1
    while dq:
        here = dq.popleft()
        if here == n:
            break
        for nxt in trees[here]:
            if visited[nxt]:
                continue
            visited[nxt] = visited[here] + 1
            dq.append(nxt)
    return (n - 1) * 2 - (visited[n] - 1)


print(minimumTreePath(5, [[1, 2], [2, 3], [2, 4], [1, 5]], [3, 4]))
# print(minimumTreePath1(5, [[1, 2], [1, 3], [3, 4], [3, 5]], [2, 4]))

print(minimumTreePath(6, [[1, 6], [1, 3], [2, 5], [1, 5], [3, 4]], [1, 5]))
# Expected Output : 3

"""
1
3   5   6
4   2
"""
