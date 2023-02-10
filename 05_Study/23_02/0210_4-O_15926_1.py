'''
< 현욱은 괄호왕이야! >
https://www.acmicpc.net/problem/15926
문제)
- 괄호 문자열중 가장긴 부분의 문자열의 길이를 계산
입력)
- 1     : n ~ [1 \ 200,000]
- 2     : 괄호문자열
'''
n = int(input())
s = input().rstrip()
d = [0] * (n + 1)
stk = []
for i in range(n):
    if s[i] == '(': stk.append(i)
    elif stk:  # 스택에 원소가 있고 반대 괄호이면
        d[i] = d[stk.pop()] = 1
cnt = 0
ret = 0
for i in range(n):
    if d[i]:
        cnt += 1
        ret = max(ret, cnt)
    else: cnt = 0

print(ret)
'''
- 유효한 괄호 부분을 1로 표시하는방법
    - 최종적으로는 한번더 전체 탐색하여 연속된 1은 숫자롤 올려준다.
- **로직**
- 스택활용 : for문 i : 0 ~ n-1
    - 정방향괄호 : '(' 이면 i-push
    - 반대방향괄호 :
        - stk에 잇는 경우
            - 그 i부분 1 stk top도 1 저장
            - d[i]=d[stk.pop()]=1
        - stk에 원소 없는 경우루
            - continue 
'''