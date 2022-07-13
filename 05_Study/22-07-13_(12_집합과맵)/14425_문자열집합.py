'''
총 N개의 문자열로 이루어진 집합 S가 주어진다.
입력으로 주어지는 M개의 문자열 중에서 
집합 S에 포함되어 있는 것이 몇 개인지 구하는 프로그램
입력)
    - 문자열의 개수 N, M
    - N개의 줄에는 집합 S에 포함되어 있는 문자열들이 주어진다.
    - M개의 줄에는 검해야하는 문자열들이 주어진다.
출력)
    - 총 몇개가 포함되어있는지 출력
'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
_set = set()
_list = list()
for _ in range(N):
    _set.add(input().strip())
for _ in range(M):
    _list.append(input().strip())
# _ans = _set & _check
# print(len(_ans))
ans = 0
for i in _list:
    if i in _set:
        ans += 1
print(ans)