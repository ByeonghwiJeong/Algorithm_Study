'''
< 여행가자 >
https://www.acmicpc.net/problem/1976
문제)
- 도시 N개
- 각도시 사이에 길 ( 양방향 )
- 도시들이 가능한지 여부
입력)
- 1     : 도시수 N ~ [2 \ 200]
- 2     : 여행계획에 속한 도시들의 수 M
- 3[N]  : row~i col~j
        - i도시 j도시 연결정보
        - 1연결, 0노연결
- 4     : 여행계획
'''
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

# 자기 자신으로 하는 
parent = [i for i in range(N + 1)]

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드를 찾을때까지 따라들어가며 재귀호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b: 
        parent[b] = a
    else:
        parent[a] = b

for i in range(1, N + 1):
    graph = list(map(int, input().split()))
    for index, v in enumerate(graph):
        if v == 1:
            union_parent(parent, i, index + 1)
        
tour = list(map(int, input().split()))
result = set([find_parent(parent, i) for i in tour])

if len(result) == 1: print("YES")
else: print("NO")


