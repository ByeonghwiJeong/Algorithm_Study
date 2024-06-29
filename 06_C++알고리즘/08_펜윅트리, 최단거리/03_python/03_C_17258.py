"""
https://www.acmicpc.net/problem/17258
백준 17258. 인기가 넘쳐흘러, P5
- 욱제는 수많은 사람들에게 초대장을 보냈음
- 파티인원이 T명 미만 : 퇴장
- 파티인원이 T명 이상 : 참여
- 파티가 진행되는 동안 T명 이상 유지가 힘들어, K명의 영선이 친구를 초대
- 영선이 친구들은 T명 이상이 되는 순간 다같이 파티장에서 나가버리고 돌아오지 않는다.
    - 파티 인원이 T명 이상이면 영선이의 친구들은 파티장에 들어가지 않는다.
    - 아직 들어오지 않은 영선이의 친구들은 이후 T미만이 되는 순간 들어올 수 있다.
- 영선이 친구들을 적절히 투입시켜 욱제를 파티에서 오래머물도록 하자 
입력)
- 파티가 진행되는 시간 N ~ [1, 300]
- 파티에 초대한 사람 수 M ~ [1, 300]
- 영선이의 친구 수 K ~ [1, 300]
- 욱제가 기대하는 최소의 파티 인원 T ~ [1, M]
- N, M, K, T
- M줄 ~ i번째 사람이 파티에 머무는 시간
    - ai, bi : ai시각  참여, bi시각 퇴장
- 출력파티가 시작되는 시각
"""
import sys
input = sys.stdin.readline

def go(here, num, prev):
    if here == len(v):
        return 0
    if dp[here][num] != -1:
        return dp[here][num]

    cost = max(0, t - v[here][1])
    real_cost = 0 if prev >= cost else cost - prev

    if num - real_cost >= 0:
        dp[here][num] = max(go(here + 1, num - real_cost, cost) + v[here][0], go(here + 1, num, 0))
    else:
        dp[here][num] = go(here + 1, num, 0)
    
    return dp[here][num]


n, m, k, t = map(int, input().split())
cnt = [0] * 301
dp = [[-1] * 301 for _ in range(301)]

v = []

for _ in range(m):
    a, b = map(int, input().split())
    for i in range(a, b):
        cnt[i] = min(t, cnt[i] + 1)

temp = cnt[1]
_count = 1

for i in range(2, n + 1):
    if temp != cnt[i]:
        v.append((_count, temp))
        _count = 0
        temp = cnt[i]
    _count += 1
    
v.append((_count, temp))

print(go(0, k, 0))