'''
가장 윗줄에 1부터 N까지의 숫자가 한 개씩 적혀 있다. 
그리고 둘째 줄부터 차례대로 파스칼의 삼각형처럼 위의 두개를 더한 값이 저장되게 된다. 
3 1 2 4
 4 3 6
  7 9
   16
F는 16
'''
import sys
def dfs(L, sum):
    if L == N and sum == F:
        print(*p, end=' ')
        sys.exit(0)
    else:
        for i in range(1, N+1):
            if not visited[i]:
                visited[i] = 1
                p[L] = i
                dfs(L+1, sum+p[L]*b[L])
                visited[i] = 0




N, F = map(int, input().split())
p = [0] * N
b = [1] * N
visited = [0] * (N + 1)
for i in range(1, N):
    b[i] = b[i - 1] * (N - i) // i
dfs(0, 0)

'''
1 3 3 1
1 4 6 4 1을 기준으로
for i in range(1, N):
    b[i] = b[i - 1] * (N - i) // i
위와같이 표현
sys.exit(0) 프로그램 종료
'''