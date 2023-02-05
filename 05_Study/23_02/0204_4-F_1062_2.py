'''
< 가르침 >
https://www.acmicpc.net/problem/1062
문제)
- K개의 글자만 안다.
- 남극의 단어는 "anta"으로 시작 ~ "tica"로 끝난다.
- 남극언어에 단어는 N개 밖에 없다고 가정
- 학생들이 읽을 수 있는 단어의 최댓값?
입력)
- 1     : 단어의 개수N 아는 글자K
- 2[N]  : N개의 남극단어
출력)
K개의 글자를 알때 읽을수 있는 단어 개수의 최댓값?
'''
from itertools import combinations
import sys
N, K = map(int, input().split())
first = set(['a', 'c', 'i', 'n', 't'])
words = [set(input().rstrip()[4:-4]) - first for _ in range(N)]
remain = set(chr(i) for i in range(ord('a'), ord('z') + 1)) - first

if K < 5: print(0); exit()
elif K == 26: print(N); exit()

ans = 0
for i in combinations(remain, K-5):
    readcnt = 0
    for word in words:
        # 단어 - 읽을수있는 단어 : 0이아니면 못읽음
        if word - set(i): continue
        readcnt += 1
    ans = max(readcnt, ans)
    
print(ans)

'''
pypy ❌
python ❌

실수 set(i) : combinations을 set해도 내부 원소는 tuple이다
'''