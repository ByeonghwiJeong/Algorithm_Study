# 이진탐색 소스 코드 (반복문 구현)
from numpy import array


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1
    return None

# n(원소의 개수)과 target을 입력받기
n, target = map(int, input().split())
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n - 1)
if result == None:
    print("원소가 존재하지 않습니다")
else:
    print(result + 1)

'''
10 7
1 3 5 7 9 11 13 17 18
>> 4
------
10 7
1 3 5 6 9 11 13 15 17 19
>> 원소가 존재하지 않습니다
'''