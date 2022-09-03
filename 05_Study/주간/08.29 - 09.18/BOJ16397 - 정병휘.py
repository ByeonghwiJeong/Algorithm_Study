'''
https://www.acmicpc.net/problem/16397
십진수 N,
T, G - 다른 정수 두개
A, B  버튼이 있다.
A :  N += 1
B :  N * 2 이후 0이 아닌 가장 높은 자릿수의 숫자가 1 줄어든다.
N이 99999를 넘어가면 탈출 실패
B버튼을 눌러서 N * 2 이후 높은자리수 -1 전에 99999를 넘게되면 실패

최대 T회 버튼 누를 수 있고, 
N을 G와 같게 만들었을 때 탈출 가능
입력)
- 1 : N [0 \ 99,999] T [1, 99,999] G[0, 99,999]
출력)
- 2 : 탈출할 수 없다면 'ANG' 출력
'''
from collections import deque
import sys
sys.setrecursionlimit(10 ** 7)

N, T, G = map(int, input().split())
visited = [False] * 100000

def cal_B(x):
    if x == 0:
        return 0
    return x * 2 - 10 ** (len(str(x * 2)) - 1)

def bfs(start, target):
    q = deque()
    q.append((start, 0))
    visited[start] = True
    while q:
        s, d = q.popleft()
        if d > T:
            break
        if s == target:
            return d
        nd = d + 1
        
        if s < 99999:
            a = s + 1
            if not visited[a]:
                q.append((a, nd))
                visited[a] = True       
        if s < 50000:
            b = cal_B(s)
            if not visited[b]:            
                q.append((b , nd))
                visited[b] = True
    return "ANG"


print(bfs(N, G))
