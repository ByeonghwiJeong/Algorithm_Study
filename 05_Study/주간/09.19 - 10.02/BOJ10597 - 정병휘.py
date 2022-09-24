'''
< 순열 장난 >
https://www.acmicpc.net/problem/10597

1 ~ N 까지 수로 이루어진 순열, 10진수, 공백으로 분리
공백을 지워버렸다.
복구하자
입력)
- 공백이 사라진 수열이 주어진다. [1 \ 50]
출력)
- 복구된 수열을 출력한다. 공백을 잊으면 안 된다.


'''
import sys

nums = input()
str_l = len(nums)
if str_l >= 10:
    l = 9 + (str_l - 9) // 2
else:
    l = str_l
_list = [str(i) for i in range(1, l+1)]
visited = [0] * (l + 1)
result = [0] * l
nums = nums + '0'

def dfs(L, N):
    if L > str_l:
        return
    if N == l:
        print(*result, sep=' ')
        sys.exit(0)
    # 1개 2개 경우
    n1 = nums[L:L+1]
    n2 = nums[L:L+2]
    if n1 in _list:
        if not visited[int(n1)]:
            visited[int(n1)] = 1
            result[N] = n1
            dfs(L + 1, N + 1)
            visited[int(n1)] = 0
    if n2 in _list:
        if not visited[int(n2)]:
            visited[int(n2)] = 1
            result[N] = n2
            dfs(L + 2, N + 1)
            visited[int(n2)] = 0
dfs(0, 0)
'''
1 ~ 9 : 1개 
10이상 : 2개
처음에 주어지는 값의 길이를 가지고 숫자가 총 몇개인지 계산을 하면서 구현시작했다.
------------------
if str_l >= 10:
    l = 9 + (str_l - 9) // 2
else:
    l = str_l
------------------

'''