'''
0으로 시작하지않는 정수 N
N의 자릿수 M
<연산>
- 1 ≤ i < j ≤ M인 i와 j
- i번 위치의 숫자와 j번 위치의 숫자를 바꾼다
- 바꾼 수가 0으로 시작하면 안 된다

연산을 K번 했을 때, 나올 수 있는 수의 최댓값
연산을 K번 할 수 없으면 -1 출력한다.
'''
from collections import deque
import copy
import sys
input = sys.stdin.readline

N, K = input().split()
M = len(N)
K = int(K)
N = int(N)
def bfs():
    global K
    q = deque()
    q.append((N, 0))
    while K:
        ans = 0        
        visited = set() 
        for _ in range(len(q)):
            x, t = q.popleft()
            nt = t + 1
            x = list(str(x))
            for i in range(M-1):
                for j in range(i+1, M):
                    tmp = copy.deepcopy(x)
                    tmp[i], tmp[j] = tmp[j], tmp[i]
                    if tmp[0] =='0':
                        continue
                    nx = int(''.join(tmp))
                    if nx not in visited:
                        ans = max(ans, nx)
                        visited.add(nx)
                        q.append((nx, nt))
        K -= 1
    return ans


result = bfs()
if result:
    print(result)
else:
    print(-1)

    

'''
visited 체크시 숫자의 범위가 크므로 set으로 하자!
visited를 원래는 연산최대횟수에따라서
1000001 x 11 형태로 visited체크를해야하지만
while문으로 한단계를 넘어갈때마다 visited를 초기화시킨다

10 1 -1같은 케이스에서 0이 출력되지않도록 bfs함수 return이 0인경우를 -1로 처리해준다
'''