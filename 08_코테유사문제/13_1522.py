'''
< 문자열 교환 >
https://www.acmicpc.net/problem/1522
문제)
- a와 b로만 이루어진 문자열
- a를 연속으로 만들기 위해서 필요한 교환횟수를 최소로
- 이문자열은 원형이므로 처음과 끝이 서로 인접해 있음
- 
'''
import sys
input = sys.stdin.readline

s = input().rstrip()
a_cnt = s.count('a')
ans = 1001
l = len(s)
for i in range(l):
    sub = ''
    if i + a_cnt >= l:
        comp = (i + a_cnt) % l
        sub = s[i:l]+s[0:comp]
    else:
        sub = s[i:i+a_cnt]
    b_cnt = sub.count('b')
    ans = min(ans, b_cnt)
print(ans)

"""
이 문제가 브루트포스인 이유는 'a'가 연속되어 나타낼 수 있는 모든 경우를 모두 탐색하고
그 중 가장 최소 교환 횟수를 구해야 하기 때문이다.

연속된 'a'인 문자열의 경우를 슬라이딩 윈도우를 통해 하나씩 탐색한다.
답이 될 수 있는 문자열을 만든 후, 처음 입력값과 비교한다.

abababababababa
aaaaaaaabbbbbbb 4
baaaaaaaabbbbbb 4
bbaaaaaaaabbbbb 4
bbbaaaaaaaabbbb 4
bbbbaaaaaaaabbb 4
bbbbbaaaaaaaabb 4
bbbbbbaaaaaaaab 4
bbbbbbbaaaaaaaa 4
abbbbbbbaaaaaaa 3
aabbbbbbbaaaaaa 4
aaabbbbbbbaaaaa 3
aaaabbbbbbbaaaa 4
aaaaabbbbbbbaaa 3
aaaaaabbbbbbbaa 4
aaaaaaabbbbbbba 3
3
"""