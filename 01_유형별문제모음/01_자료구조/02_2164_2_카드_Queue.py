'''
Queue 자료구조 활용
- 카드가 한 장 남을 때까지 반복
- step1) 제일 위에 있는 카드를 바닥에 버린다.
- step2) 제일 위에 있는 카드를 제일 아래 있는 카드 밑으로 옮긴다.
'''

from collections import deque

li = deque([i for i in range(1, int(input()) + 1)])

while len(li) >= 2:
    li.popleft() # 왼쪽이 제일 위
    li.rotate(-1) # 

print(li[0])
