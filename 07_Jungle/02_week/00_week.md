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