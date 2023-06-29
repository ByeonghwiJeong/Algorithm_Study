"""

"""

graph = []
visited = []
myEdges = []
Nodes = set()


def getUsedEdges(now):
    global graph, visited, myEdges
    visited[now] = True
    # 단말노드인 경우
    if graph[now] == []:
        if now in Nodes:
            return True
        return False

    # 단말노드가 아닌 경우
    returnValue = False
    for next in graph[now]:
        if not visited[next]:
            returnValue = getUsedEdges(next)
            if returnValue:
                myEdges.append([now, next])

    return returnValue


def minimumTreePath(n, edges, visitNodes):
    global graph, visited, myEdges, Nodes
    graph = [[] for _ in range(n + 1)]
    visited = [0] * (n + 1)
    myEdges = []
    for edge in edges:
        graph[edge[0]].append(edge[1])
    # 방문해야하는 노드
    Nodes = set(visitNodes)
    Nodes.add(1)
    Nodes.add(n)

    return 1


print(minimumTreePath(5, [[1, 2], [2, 3], [2, 4], [1, 5]], [3, 4]))
# print(minimumTreePath1(5, [[1, 2], [1, 3], [3, 4], [3, 5]], [2, 4]))
# 1 - 2 - 3
#       - 4
#   - 5
# 1 > 2 > 3
# 1 > 2 > 4
# 1 > 5
# 1 > 2 > 3 > 2 > 4 >

print(minimumTreePath(6, [[1, 6], [1, 3], [2, 5], [1, 5], [3, 4]], [1, 5]))
# Expected Output : 3
