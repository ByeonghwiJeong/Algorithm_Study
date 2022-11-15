'''
< 이진 검색 트리 > 
https://www.acmicpc.net/problem/5639
문제 : 전위순회  >>> 후위순회

입력)
50 30 24 5 28 45 98 52 60
50 || 30 24 5 28 45 | 98 52 60
    30 || 24 5 28 | 45
        24 || 5 | 28
            5
            28
        45
    98 || 52 60 |
        52 || 60
            60
출력)
5 28 24 45 30 60 52 98 50
'''
import sys
input = sys.stdin.readline

a = []
while True:
    try: n = int(input())
    except: break
    a.append(n)

def post_order(st, en):
    if st > en: return
    temp = 0
    init_v = a[st]
    for i in range(st+1, en+1):
        if init_v < a[i]:
            temp = i
            break
    else: temp = en + 1
    post_order(st+1, temp - 1)
    post_order(temp, en)
    print(init_v)

post_order(0, len(a)-1)

