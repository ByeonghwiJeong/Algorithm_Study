import sys
input = sys.stdin.readline
'''

'''
words = []
for _ in range(int(input())):
    words.append(input().strip())
words = list(set(words))
words.sort(key = lambda x:(len(x), x))
print(*words, sep='\n')
