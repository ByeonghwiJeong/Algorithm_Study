"""
https://www.acmicpc.net/problem/20920

제목: 영단어 암기는 괴로워
"""

import sys
from collections import defaultdict
input = sys.stdin.readline

N, M = map(int, input().split()) 

words = defaultdict(int)

for _ in range(N):
    word = input().strip()
    if len(word) < M:
        continue
    words[word] += 1

# 정렬 1.갯수, 2.길이, 3.알파벳순
sorted_words = sorted(words.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for word, _ in sorted_words:
    print(word)
