'''
N개의 원소로 구성된 자연수 집합
집합을 두 개의 부분집합으로 나누었을 때
두 부분집합의 원소의 합이 서로 같은 경우가 존재하면 “YES"를 출력
그렇지 않으면 ”NO"를 출력
'''
import sys
n = int(input())
_list = list(map(int, input().split()))
total = sum(_list)
chk = [0] * n

def dfs(L):
    if L == n:
        sum1 = 0
        sum2 = 0
        for i in range(n):
            if chk[i] == 1:
                sum1 += _list[i]
            else:
                sum2 += _list[i]
        if sum1 == sum2:
            print('YES')
            sys.exit(0)
    else:
        chk[L] = 1
        dfs(L + 1)
        chk[L] = 0
        dfs(L + 1)

dfs(0)
print('NO')
'''
구현방법 1)
- chk방식 (내풀이)
구현방법 2)
- dfs함수에서 매개변수를 길이와 합을 같이 넘기는 방식
- dfs(L, sum)
특정 조건에서 프로그램을 종료하는법 sys.exit(0)
'''