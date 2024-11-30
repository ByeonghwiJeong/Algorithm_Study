'''
https://www.acmicpc.net/problem/7490
제목: 0 만들기

문제)
- 1부터 N까지의 수를 오름차순으로 쓴 수열 1 2 3 ... N을 생각하다.
- '+'나 '-', 또는 ' '(공백)을 숫자 사이에 삽입
- 공백은 숫자를 이어줌


입력)
- 1 : 테스트 케이스의 개수 T ~ [1, 10]
- 2 ~ T+1 : 수 N ~ [3, 9]


입력 예시)
2
3
7
출력 예시)
1+2-3

1+2-3+4-5-6+7
1+2-3-4+5+6-7
1-2 3+4+5+6+7
1-2 3-4 5+6 7
1-2+3+4-5+6-7
1-2-3-4-5+6+7
'''
import sys
input = sys.stdin.readline


def dfs(N, idx, exp):
    if idx == N:
        if eval(exp.replace(' ','')) == 0:
            print(exp)
        return
    
    dfs(N, idx + 1, exp + ' ' + str(idx + 1)) # ???? 왜 순서에 따라서? -> ASCII 순서
    dfs(N, idx + 1, exp + '+' + str(idx + 1))
    dfs(N, idx + 1, exp + '-' + str(idx + 1))
    

for _ in range(int(input())):
    N = int(input())
    dfs(N, 1, '1')
    print()