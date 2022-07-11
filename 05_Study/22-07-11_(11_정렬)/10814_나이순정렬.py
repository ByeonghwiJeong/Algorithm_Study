'''
첫째줄 : 회원수 ~100,000
둘째줄 : N개줄 / 회원의나이와 이름

가입한 순 처리

원인...???
--- x[0] >> int화
'''
import sys
input = sys.stdin.readline

members = []
for i in range(int(input())):
    a = list(input().split())
    a.append(i)
    members.append(tuple(a))
print(members)
members.sort(key = lambda x:(int(x[0]), x[2]))
print(members)
for m in members:
    print(m[0], m[1])