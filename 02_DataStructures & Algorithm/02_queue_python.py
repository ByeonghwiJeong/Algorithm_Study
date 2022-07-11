'''
리스트 자료로 구현 x
시간복잡도 ㅜㅜ
'''
from collections import deque

# 큐(Queue) 구현을 위해 deque 라이브러리 사용
q = deque()

# 삽입(5, 2, 3, 7) - 삭제() - 삽입(1, 4) - 삭제()
q.append(5)
q.append(2)
q.append(3)
q.append(7)
q.popleft()
q.append(1)
q.append(4)
q.popleft()

print(q) # 먼저 들어온 순서대로 출력
# deque([3, 7, 1, 4])
q.reverse()
print(q) # 최하단 원소부터 출력
# deque([4, 1, 7, 3])
