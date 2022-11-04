'''
< 괄호 >
https://www.acmicpc.net/problem/9012
문제)
- 
입력)
- 
출력)
- 
'''
import sys
input = sys.stdin.readline

def go(s):
    l = []
    for i in s:
        if i == "(":
            l.append(i)
        else:
            if l: l.pop()
            else: return "NO"
    if l: return "NO"
    else: return "YES"

for _ in range(int(input())):
    s = input().rstrip()
    print(go(s))
