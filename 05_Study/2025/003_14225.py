'''
https://www.acmicpc.net/problem/14225
제목 : 부분수열의 합

문제)
- 수열 S의 부분 수열의 합으로 나올 수 없는 가장 작은 자연수를 구하는 프로그램을 작성
- S = [5, 1, 2]인 경우에 1, 2, 3(=1+2), 5, 6(=1+5), 7(=2+5), 8(=1+2+5)을 만들 수 있다
- 4는 만들 수 없기 때문에 정답은 4

입력)
3
5 1 2

출력)
4
'''
import sys
input = sys.stdin.readline

N = int(input())
S = list(map(int, input().split()))

sum_set = set()

def dfs(idx, sum):
    if idx == N:
        return
    sum_set.add(sum + S[idx])
    dfs(idx + 1, sum + S[idx])
    dfs(idx + 1, sum)

dfs(0, 0)

for i in range(1, 1000000):
    if i not in sum_set:
        print(i)
        break
