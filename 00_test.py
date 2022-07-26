import heapq

_list = [32, 16, 54, 94, 81, 31]
# heapq 는 리스트 기반 자료구조
heapq.heapify(_list)
# 기존 list를 heapify를 사용해 배치
heapq.heappush(_list, 7)
# heappush : 값을 heap에 넣음
print(heapq.heappop(_list))
# heappop : heap에 있는 값 중 최솟값을 뺌
print(heapq.heappushpop(_list, 100))
# heappushpop : push & pop
small_elements = heapq.nsmallest(4, _list)
print(small_elements)
# nsmallest : heap원소 중 최솟값 n개 리턴
large_elements = heapq.nlargest(4, _list)
print(large_elements)
