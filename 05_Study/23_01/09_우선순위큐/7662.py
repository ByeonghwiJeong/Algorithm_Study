'''
< 이중 우선 순위 큐 >
- 최대힙 & 최소힙 두가지 저장
- 다른 힙에서 이미 제거된 값을 판단하기위해 \
    큐에 값이 들어올때마다 is_valid에 상태 저장
- 만약 최대최소 힙에서 값을 꺼냈을 때\
    해당 인덱스의 is_valid원소가 False로 표기되어 있다면,\
        이미 다른 큐를 통해 제거된 값이므로 버리고 다시꺼내야한다.
'''
import sys
import heapq as hq
input = sys.stdin.readline
T = int(input())

# 힙에서 유효하지 않은 값 삭제하는 함수
def remove_invalid_data(heap):
    # 힙에 데이터가 하나라도 있고, top이 invalid(False)하면 pop해줌
    while heap and not is_valid[heap[0][1]]:
        hq.heappop(heap)
    return

for _ in range(T):
    t = int(input())

    max_heap = []
    min_heap = []
    is_valid = []
    idx = 0
    # 이번에 들어올 값의 인덱스,
    # is_valid[idx]에 값이 유효성이 저장된다.
    for _ in range(t):
        cmd, n = input().split()
        if cmd == 'D': # 삭제
            if n == '1':    #  최댓값 삭제
                remove_invalid_data(max_heap)
                if max_heap:
                    # 값을 제거후 유효성을 갱신
                    is_valid[hq.heappop(max_heap)[1]] = False
            else:           #  최솟값 삭제
                remove_invalid_data(min_heap)
                if min_heap:
                    is_valid[hq.heappop(min_heap)[1]] = False   
        else: # 추가
            hq.heappush(max_heap, (-int(n), idx))
            hq.heappush(min_heap, (int(n), idx))
            is_valid.append(True) 
            idx += 1
    
    remove_invalid_data(max_heap)
    remove_invalid_data(min_heap)

    if max_heap: print(-max_heap[0][0], min_heap[0][0])
    else: print("EMPTY")