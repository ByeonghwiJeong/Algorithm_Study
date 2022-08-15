'''
1. 현재 Queue의 가장 앞에 있는 문서의 '중요도'를 확인한다.
2. 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면, 
이 문서를 인쇄하지 않고 Queue 가장 뒤에 재배치 한다.
그렇지 않다면 바로 인쇄한다.

ex)
A B C D
2 1 4 3

C D A B 

C D A B

1 2 3 4
4 1 2 3 / 4
3 1 2 / 3
2 1 / 2
1 / 1
입력)
    - 1 : 테스트 케이스 수
        - test1 : 문서의 개수 N ; [1,100]
                몇 번째로 인쇄되었는지 궁금한 문서가 
                현재 Queue에서 몇 번째 놓여 있는지 M [0,N)
        - test2 : N개 문서 의 중요도
        -  

6 0 
1 1 9 1 1 1
'''
from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N, M = map(int, input().split())
    q = deque(list(input().split()))
    index_q = deque([i for i in range(N)])
    cnt = 0
    while q:
        if q[0] == max(q):
            x = q.popleft()
            i = index_q.popleft()
            cnt += 1
            if M == i:
                print(cnt)
                break
        else:
            q.rotate(-1)
            index_q.rotate(-1)
