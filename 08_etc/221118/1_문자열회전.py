'''
배열 회전 !!!!!
배열 주소값
[7, 8, 9] >>>> 크기가 N이면 O(N-1):O(N) - 빅오표기법  
A = [8, 9] + [7] >>>> O(1)
배열은 조회하는데 O(1)
배열은 삭제하는데는 O(N)
    - 앞쪽 index 0부분을 삭제하는데는 N만큼걸리고
    - 뒤에 index N-1 ( A.pop() ) : 1
    - 빅오표기법으로는 최악의 상황을 고려하기때문에
        O(N)
deque : double ended queue - 양방향큐
    - 파이썬 특성상 deque 이게 속도 빨라서
    - 검색해보기 deque vs queue
queue라는 자료구조 First in First out
    -
stack이라는 자료구조 First in Last out
  - List.append() or List.pop()

< Queue 자료구조 문제 >
'''
from collections import deque
def solution(arrA, arrB):
    q1 = deque(arrA)
    q2 = deque(arrB)
    for _ in range(len(arrA)):
        # q1.rotate(1)
        a = q1.popleft() # O(1)
        q1.append(a) # O(1)
        # q1.append(q1.popleft())
        # ABC 
        # BCA CAB ABC
        if q1 == q2: return True
    return False

print(solution([7, 8, 10], [10, 7, 8])) # True
print(solution([4, 3, 2, 1], [5, 4, 1, 2])) # False