'''
< 휴게소 세우기 >
https://www.acmicpc.net/problem/1477
문제)
- 다솜이는 휴게소 N개 가지고 있다.
- 휴게소의 위치는 고속도로로 부터 얼만큼 떨어져 있는지?
- M개를 더 세우려고 한다.
- 다솜이는 휴게소를 M개 더 지어서 휴게소가 없는 구간의 길이의 최대값을 최소로 하려고 한다.
( M개를 모두 지어야 한다. )
입력)
- 1      : 휴게소의 개수 N, 더 지을 휴게소의 개수 M, 고속도로의 길이 L
- 2      : 휴게소의 위치
'''
import sys
input = sys.stdin.readline

n, m, l = map(int, input().split())
location = list(map(int, input().split()))
location.append(0)
location.append(l)
location.sort()
n = n + 2 # 양쪽 끝 추가

# m개의 휴게소를 추가해서 휴게소 없는 구간이 dist 이하로 만들수 있는지?
def check(mid):
    cnt = 0
    for i in range(n-1):
        cnt += (location[i+1] - location[i] - 1) // mid
    return cnt <= m

def binary_search():
    left, right = 1, l -1
    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            right = mid - 1
        else:
            left = mid + 1
    return right + 1

print(binary_search())

'''
'''