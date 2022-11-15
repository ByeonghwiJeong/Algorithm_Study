'''
< 트리 순회 > 
https://www.acmicpc.net/problem/1991
문제 - 전위, 중위, 후위
- 전위Pre-order : (루트)(왼쪽)(오른쪽) 
- 중위in-order : (왼쪽)(루트)(오른쪽)
- 후휘post-order : (왼쪽)(오른쪽)(루트)
입력)
- 노드의 개수 N [1 \ 26]
'''
import sys
input = sys.stdin.readline

n = int(input())
a = [[] for _ in range(26)]

def alpa_chk(x):
    if x == '.': return None
    return ord(x) - ord('A')

for _ in range(n):
    p, c1, c2 = map(alpa_chk, input().split())
    a[p].append(c1)
    a[p].append(c2)

def pre_order(n):
    if n == None: return
    print(chr(n+65), end='')
    pre_order(a[n][0])
    pre_order(a[n][1])

def in_order(n):
    if n == None: return
    in_order(a[n][0])
    print(chr(n+65), end='')
    in_order(a[n][1])
        

def post_order(n):
    if n == None: return
    post_order(a[n][0])
    post_order(a[n][1])
    print(chr(n+65), end='')


pre_order(0)
print()
in_order(0)
print()
post_order(0)
