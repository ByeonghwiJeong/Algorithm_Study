"""
< 완전 이진 트리 >
https://www.acmicpc.net/problem/9934
문제)
- 깊이가 K 완전이진트리는 총 2^K - 1개의 노드로 이루어져 있다.
- 마지막 레벨을 제외한 모든 집은 왼쪽 오른쪽 자식을 갖는다.
- 상근이는 도시에 있는 모든 빌딩에 들어갔고, 들어간 순서대로 번호를 적었다.
- 어떤 순서로 도시를 방문했는지 기억했다.
    - 1. 가장 처음 투리의 투르에 있는 빌딩 앞에 서있다.
    - 2. 현재 빌딩에 왼쪽 자식에 방문하지않았다면 왼쪽 자식으로 이동
    - 3. 왼쪽 자식을 가지고 있지 않거나, 왼쪽 자식 빌딩 방문했으면
            현재 노드에 있는 빌딩을 들어가고 종이에 번호를 적는다.
    - 4. 현재 빌딩을 이미 들어갔다 온 상태이고, 
            오른쪽 자식을 가지고 있는경우에 오른쪽 이동
    - 5. 왼쪽 오른쪽 자식 방문했으면, 부모 노드로 이동

입력)
- 1     : 깊이 K
- 2     : 
출력)
- 1
"""
import sys
input = sys.stdin.readline

K = int(input())
a = list(map(int, input().split()))
ret = [[] for _ in range(K)]

def go(st, en, l):
    global ret
    if st == en: 
        ret[l].append(a[st])
        return
    mid = (st + en) // 2
    ret[l].append(a[mid])
    go(st, mid - 1, l + 1)
    go(mid + 1, en, l + 1)
    return

go(0, 2**K-2, 0)
for i in ret:
    print(*i)
    
    
"""
0 0 0 0
2^k - 1
1
3
7
15 index 14 // 2 = 7
"""