'''
< 오큰수 >
https://www.acmicpc.net/problem/17298
문제)
- 크기 N인 수열 A1, A2, A3 ... AN
- 원소Ai에 대해서 오큰수 NGE(i)
    - 오른쪽에 있으면서 Ai보다 큰 수 중에서 가장 왼쪽에 있는 수를 의미
    - 없는경우 -1
- A = [9, 5, 4, 8] : -1, 8, 8, -1

'''

import sys
input = sys.stdin.readline

N = int(input())
a = list(map(int, input().split()))
s = []
ans = [-1] * N
for i in range(N):
    while s and a[s[-1]] < a[i]:
        ans[s.pop()] = a[i]
    s.append(i)
print(*ans)

'''
### 스택 자료구조 활용
- for 1 ~ N:
    - while :스택에 자료가 있고 \ 값[스택top]보다 오른쪽수가 더 크면
        - ans[스택top] = 오른쪽수
        - 스택pop
    - index를 스택에 넣기
'''