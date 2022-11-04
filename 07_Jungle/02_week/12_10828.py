'''
< 스택 >
https://www.acmicpc.net/problem/10828
문제)
- 
입력)
- 
출력)
- 
'''
import sys
input = sys.stdin.readline

l = []
for _ in range(int(input())):
    s = input().split()
    if len(s) == 2:
        l.append(s[1])
    else:
        if s[0] == "top":
            if l: print(l[-1])
            else: print(-1)
        elif s[0] == "size":
            print(len(l))
        elif s[0] == "empty":
            if l: print(0)
            else: print(1)
        elif s[0] == "pop":
            if l: print(l.pop())
            else: print(-1)
    