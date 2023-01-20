'''
< 가희와 키워드 >
https://www.acmicpc.net/problem/22233
문제)
- 메모장에 서로 다른 키워드 총 N개가 존재
- 글을 작성시 최대 10개의 키워드에 대해서 글 작성
    - 이 키워드들 중에 메모장에 있었던 키워드는 글 작성이후 삭제
- 글작성후 메모장에 있는 키워드 개수는?
입력)
- 1     : 메모장 키워드 개수 N, 가희가 블로그에 쓴 글의 개수 M
            - N ~ [1 \ 2x10^5]
            - M ~ [1 \ 2x10^5]
- 2[N]  : 메모장 키워드
- 3[M]  : 글 키워드 (,로구분)
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = set([input().rstrip() for _ in range(n)])
for _ in range(m):
    b = input().rstrip().split(',')
    for i in b:
        if i in a: a.remove(i)
    print(len(a))
