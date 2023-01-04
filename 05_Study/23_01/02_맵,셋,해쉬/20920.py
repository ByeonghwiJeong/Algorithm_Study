'''
< 영단어 암기는 괴로워 >
문제) 단어장의 단어 순서
- 자주 나오는 단어일수록 앞에 배치
- 길이가 길수록 앞에 배치
- 알파벳 사전 순으로 앞에 있는 단어 일수록 앞에 배치

- 길이가 M 이상인 단어들만 외운다
입력) 
- 1     : 단어개수N, 기준길이M
- 2[N]  : 단어
'''
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
# a = []
b = dict()
for _ in range(N):
    c = input().rstrip()
    if len(c) < M: continue
    if c in b:
        b[c] += 1
    else:
        b[c] = 1
# print(b)
a = sorted(b.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
for i in a:
    print(i[0])