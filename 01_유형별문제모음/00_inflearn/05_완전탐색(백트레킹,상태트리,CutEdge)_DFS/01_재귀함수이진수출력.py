'''
<재귀방식>
10진수 N[1 \ 1000]이 입력되면 2진수 변환하여 출력
11
1101
'''
def dfs(x):
    if x == 0:
        return
    dfs(x // 2)
    print(x % 2, end='')

n = int(input())
dfs(n)