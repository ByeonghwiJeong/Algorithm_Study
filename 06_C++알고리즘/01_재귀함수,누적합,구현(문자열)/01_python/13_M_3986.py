'''
https://www.acmicpc.net/problem/3986
제목 : 좋은 단어

문제
- A와 B로만 이루어진 단어가 있다.
- 좋은 단어는 다음과 같다.
- 같은 글자끼리 짝을 짓는다 (아치형 곡선을 그어서)
- 선이 교차하지 않는다.


'''
import sys
input = sys.stdin.readline

def is_good_word(word):
    stack = []
    for c in word:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
    return not stack

N = int(input())
cnt = 0

for _ in range(N):
    if is_good_word(input().strip()):
        cnt += 1

print(cnt)