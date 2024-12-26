"""
https://www.acmicpc.net/problem/2668

제목: 숫자고르기


"""
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
inputs = [0] + [int(input()) for _ in range(N)]
answer = set()

def find_cycle(start):
    visited = set()
    current = start

    while current not in visited:
        visited.add(current)
        current = inputs[current]

    
    # 사이클이 존재하는 경우
    if current == start:
        return visited
    return set()


result = set()
for i in range(1, N+1):
    if i in result:
        continue
    result.update(find_cycle(i))

print(len(result))
print(*sorted(result), sep="\n")    
