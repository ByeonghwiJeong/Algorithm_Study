import sys
input = sys.stdin.readline

l = [input().rstrip() for _ in range(int(input()))]
l = list(set(l))
l.sort(key=lambda x : (len(x), x))
print(*l, sep='\n')