"""
1. 아이디어
- 투포인터를 활용
- for문으로, 처음에 K개값을 저장
- 다음인덱스 더해주고, 이전 인덱스 빼줌
- 이때마다 최대값을 갱신
2. 시간복잡도
- O(N) = 1e5 > 가능
3. 자료구조
- 각 숫자들 N개 저장 배열 : int[]
    - 숫자들 최대 100 > INT 가능
- K개의 값을 저장 변수 : int
    - 최대 : K * 100 = 1e5 * 100 = 1e7 > INT가능
- 최대값, : int
<문제>
https://www.acmicpc.net/problem/2559
"""
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
nums = list(map(int, input().split()))
maxv = []

for i in range(N-K+1):
  maxv.append(sum(nums[i:K+i]))

print(max(maxv))

