'''
팰린드롬 문자열  >>  대칭문자열
같은 알파벳 최대 1문자만 홀수개
나머지는 알파벳은 전부 짝수개

입력)
    알파벳 대문자로만 된 최대 50글자



[[  ]]
'''
from collections import Counter
c = Counter(input())
'''
c = dict()
s = input()
for ch in s:
# 키값있는지 확인 할때 <확인할키값> in <dict>  
    if ch in c:
        c[ch] += 1
    else:
        c[ch] = 1
# Counter 방식을 for ~~ if in dict ~ else 구문으로 구현
'''
if sum(i % 2 for i in c.values()) > 1:
    ans = "I'm Sorry Hansoo"
else:
    half = ''
    center = ''
    for k, v in sorted(c.items()):
        half += k * (v//2)
        if v % 2:
            center = k
    ans = half + center + half[::-1]
# 문자열 뒤집기 
# ''.join(reversed(half))
print(ans)

