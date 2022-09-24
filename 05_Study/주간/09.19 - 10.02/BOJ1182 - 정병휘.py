'''
<부분수열의 합>
https://www.acmicpc.net/problem/1182

N개의 정수로 이루어진 수열이 있을 때, 
크기가 양수인 부분수열 중에서
그 수열의 원소를 다 더한 값이 S가 되는 경우의 수를 구하는 프로그램
입력)
- 1 : 정수의 개수 N [1 \ 20], 정수 S [-1,000,000 \ 1,000,000]
- 2 : 둘째 줄에 N개의 정수가 빈 칸을 사이에 두고 주어진다
출력)
- 1 : 첫째 줄에 합이 S가 되는 부분수열의 개수를 출력한다.
'''
N, S = map(int, input().split())
_list = list(map(int, input().split()))
result = 0

def dfs(L, sum):
    global result
    if L == N:
        if sum == S:
            result += 1
        return
    dfs(L+1, sum+_list[L])
    dfs(L+1, sum)

dfs(0, 0)
if S == 0: # 이부분을 생각하기 힘들었음
    result -= 1
print(result)

'''
계속 오류가 발생해서 보니 모든 원소를 선택하지않았을경우에 sum은 0이 되고
그 경우에 S가 0이면 result 갯수가 1개 늘어난다.
'''