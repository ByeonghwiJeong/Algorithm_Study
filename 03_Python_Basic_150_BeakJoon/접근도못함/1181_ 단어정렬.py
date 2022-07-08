'''
정렬 기준 2가지

- 1순위 : 단어길이
- 2순위 : 영단어순

리스트에 (길이, 단어) 형태로 append후 sort
'''

n = int(input())

words = []
for i in range(n):
    words.append(input())

set_words = list(set(words))

sort_words = []
for i in set_words:
    sort_words.append((len(i), i))

result = sorted(sort_words)

for a, b in result:
    print(b)