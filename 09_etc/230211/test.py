def a():
    global visited
    visited[1] = 1

def solution():
    visited = [0, 0]
    a(visited)


solution()