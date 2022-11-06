# Jungle_02_week CheckPoint

### 1920 - 수 찾기
https://www.acmicpc.net/problem/1920
- 재귀적으로 binary_search함수를 호출하면서 return하는형태
- **함수내부에서 호출시 return이후에 호출하자!!**

### 2805 - 나무 자르기
https://www.acmicpc.net/problem/2805
- 파라메트릭서치
- **반대방향**
- mid를 올릴수록(절단기높이) 가지고가는 나무(hight_sum)는 줄어든다
- hight_sum < target : hight_sum를 올리기위해서 낮은범위 탐색
- **정렬할필요없음**

### 2110 - 공유기 설치 ⭐⭐⭐ 
https://www.acmicpc.net/problem/2110
- 파라메트릭서치
- 기준 : 공유기거리 ~ 정렬된a대하여
    - a[-1] - a[0] 에서 시작
- st, en에 따른 공유기개수 함수선언
- 이분탐색함수 : **리턴값**
    - 개수 >= 타겟 : ⭕공유기 거리를 늘릴때 mid값⭕
    - 개수 < 타겟 : ❌공유기 거리를 줄일때 mid값❌

### 2110 - 용액 문제  
https://www.acmicpc.net/problem/2470
- 투포인터 or 이진탐색


### 11053 - 가장 긴 증가하는 부분 수열
https://www.acmicpc.net/problem/11053
- dp방식
- **기본으로 주어진 배열과 dp배열앞 '0'추가**
- dp[i]는 A[i]보다 작은 A[j] 중 가장 큰 dp[j]값에 1을 더한값


### 12015 - 가장 긴 증가하는 부분 수열
https://www.acmicpc.net/problem/12015
- 이진탐색 && **스택**

### 8993 - 사냥꾼
https://www.acmicpc.net/problem/8983
- 동물의 x좌표를 기준으로 정렬된사로x위치중 가까운것 선택
- 반례처리 : bisect_left기준 반환값 0 or len(x) 일경우
    - 각각 x[0], x[-1] 반환
    
### 2812 - 크게 만들기
https://www.acmicpc.net/problem/2812
- 기본적인 스택문제 
- 특수한 조건인 k가 while문을 다돌았을때 0이아닌경우
    - stack 뒤에 k개만큼 날리기
    - input: 4 2 // 4321

### 2164 - 카드2
https://www.acmicpc.net/problem/2164
- **collections.deque**
    - q.append(q.popleft())
    - q.rotate(-1)

### 3190 - 뱀
https://www.acmicpc.net/problem/3190
- **그냥 다시풀자**

### 11279 - 최대힙
https://www.acmicpc.net/problem/11279
- heapq : 최소힙으로 구성
- 최대힙구현하려면 heapq.heappush(_list, (-x, x))
- heapq.heappop(_list)

