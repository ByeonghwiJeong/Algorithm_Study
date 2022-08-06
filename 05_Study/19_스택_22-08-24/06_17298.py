'''
수열 A1 ~ An
오큰수 NGE(i) : 오른쪽에 있으면서 Ai보다 큰 수 중 가장 왼쪽
    - 없으면 -1

A = 3, 5, 2, 7 + 0
    5  7  7  -1
deque
3 5
3
5
  5 2 7

A = 5 9 4 8 + 0
5
9 4
9

<< 과정 >>
1. 초기값이 -1 인 크기N인 리스트 _list 선언
2. for loop : 0 ~ N-1 
    - stack에 원소가 있는경우 while문 실행
        - _list[ i ]와 _list [ _stack의 마지막값 ] 크기 비교
            => _list[ i ] > _list[_stack[-1]] 인경우
                ans[_stack[-1]] = _list[i]
            => 그외 : break
    - stack에 index뜻하는 i를 append
'''

import sys
input = sys.stdin.readline

N = int(input())
_list = list(map(int, input().split()))
_stack = list()
ans = [-1] * N
for i in range(N):
    while _stack:
        if _list[i] > _list[_stack[-1]]:
            ans[_stack.pop()] = _list[i]
        else:
            break
    _stack.append(i)

print(*ans)