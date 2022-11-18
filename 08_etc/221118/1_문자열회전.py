from collections import deque


def solution(arrA, arrB):
    q1 = deque(arrA)
    q2 = deque(arrB)
    for _ in range(len(arrA)):
        q1.rotate(1)
        if q1 == q2: return True
    return False

print(solution([7, 8, 10], [10, 7, 8]))
print(solution([4, 3, 2, 1], [5, 4, 1, 2]))