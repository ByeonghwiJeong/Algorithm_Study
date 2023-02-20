'''
< 1학년 >
https://www.acmicpc.net/problem/5557
문제)
- 마지막 두 숫자 사이에 '='
- 나머지 숫자 사이에는 '+' '-'
- 중간에 나오는 수가 모두 0이상 20이하
    - "8+3+2-4-8-7+2+4+0+8=8"은 올바른 등식이지만, 
    - 8+3+2-4-8-7이 음수이므로 만들수 없다.
- 올바른 등식의 수
입력)
- 1     : 숫자의 갯수 N ~ [3 \ 100]
- 2     : N개의 숫자
출력)
- 1     : 올바른 등식의 개수
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

def recur(idx, _sum):
    global dp
    if _sum < 0 or _sum > 20: return 0
    ret = dp[idx][_sum]
    if ret: return ret
    if idx == N - 2:
        if _sum == a[N - 1]: return 1
        return 0
    ret += recur(idx + 1, _sum + a[idx + 1])
    ret += recur(idx + 1, _sum - a[idx + 1])
    dp[idx][_sum] = ret
    return ret

    
N = int(input())
a = list(map(int, input().split()))
dp = [[0] * 21 for _ in range(104)]
print(recur(0, a[0]))


'''
C++ : 레퍼런스 참조
'''