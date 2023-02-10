'''
< 컵라면 >
https://www.acmicpc.net/problem/1781
문제)
- 상욱조교는 동호에게 N개의 문제를 준다.
- 각각의 문제를 풀었을 때 컵라면을 몇 개 줄 것인지 제시
- 데드라인 존재
- 동호가 받을 수 있는 최대 컵라면 수???
입력)
- 1     : 숙제의 개수 N ~ [1 \ 200,000]
- 2[N]  : 데드라인 컵라면

'''
import sys, heapq
input = sys.stdin.readline

N = int(input())
a = [list(map(int, input().split())) for _ in range(N)]
a.sort()
hq = []
ret = 0
for i in range(N):
    ret += a[i][1]
    heapq.heappush(hq, a[i][1])
    if len(hq) > a[i][0]:
        ret -= heapq.heappop(hq)
print(ret)

'''
### 1. 라인스위핑
- 문제에는 데드라인이 있음 - 구간안에 풀어야함!!!
- ![라인스위핑](https://blog.kakaocdn.net/dn/biuYDc/btrrpEpHCiq/iOCbtB5hkcYMmtt9NEqwW0/img.png)

### 2. 배치 고려 - 정렬
- ![정렬](https://user-images.githubusercontent.com/95831345/217975364-de64b08d-7ec9-4e86-be34-75b2e778c2e2.png)
- 정렬기준 : 데드라인

### 로직
1. 데드라인기준 정렬
2. ret = 0, hq = [] 선언
3. for문 1 ~ N-1
    1. ret 에 index컵라면 더하기
    2. hq의 크기(걸리는시간) > index데드라인 - 데드라인넘는경우
        - ret에 hq의 최소값빼기(최소힙 pop)
4. ret 출력
'''