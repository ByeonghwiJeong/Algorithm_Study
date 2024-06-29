import sys
input = sys.stdin.readline

N = int(input())
pre_pattern, post_pattern = input().rstrip().split('*')
pre_len, post_len = len(pre_pattern), len(post_pattern)

for _ in range(N):
    word = input().rstrip()
    if len(word) < pre_len + post_len:
        print('NE')
        continue
    if word[:pre_len] == pre_pattern and word[-post_len:] == post_pattern:
        print('DA')
    else:
        print('NE')