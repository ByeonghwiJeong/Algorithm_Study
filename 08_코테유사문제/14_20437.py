'''
< 문자열 게임 2 >
https://www.acmicpc.net/problem/20437
문제)
- 게임진행방식
1. 알파벳 소문자로 이루어진 문자열 W
2. 양의 정수 K가 주어진다.
3. 어떤 문자를 정확히 K개를 포함하는 가장 짧은 연속 문자열의 길이를 구한다.
4. 어떤 문자를 정확히 K개를 포함하고, 문자열의 첫 번째와 마지막 글자가 해당 문자로 같은 가장 긴 연속 문자열의 길이를 구한다.
입력)
- 1     : 문자열 게임의 수 T
- 2     : 문자열 W와 정수 K
'''
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    v = input().rstrip()
    k = int(input())
    _max = 0
    _min = 10001

    # 알파벳별로 연결리스트형태로 index저장
    pos = [[] for _ in range(26)]
    for i, v in enumerate(v):
        pos[ord(v)-97].append(i)

    for p in pos:
        for i in range(len(p) - k + 1): # 2
            # 문자열 
            _min = min(_min, p[i+k-1]-p[i]+1)
            _max = max(_max, p[i+k-1]-p[i]+1)
    
    if _max: print(_min, _max)
    else: print(-1)