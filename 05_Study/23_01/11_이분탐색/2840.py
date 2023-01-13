'''
< 행운의 바퀴 >
- 같은 글자는 두 번 이상 X
- 시계방향으로만 돌아간다.
- 바퀴 옆에는 화살표가 있음
- K번 회전
- 매번 회전시, 화살표가 가리키는 글자가 변하는 횟수와 \
    어떤 글자에서 회전을 멈추었는지 종이에 적는다.
- 
입력)
- 1     : 바퀴의 칸수 N ~ [2 \ 25], 바퀴를 돌리는 횟수 K ~ [1 \ 100]
- 2[K]  : 화살표가 가리키는 글자가 몇 번 바뀌었는지???

예2)
5 6
1 A
2 B
5 B
1 C
2 A
2 B
------
[?][?][?][?][?]
[B][?][A][?][C]
B?A?C

2 B
2 A
1 C
5 B
2 B
1 A 
1
B ? A ? C
'''
import sys
input = sys.stdin.readline

def make_wheel(n, record):
    wheel = ['?'] * n   # 바퀴의 상태
    is_available = dict()   # 해당 알파벳을 새로 쓸 수 있는지 확인하는 딕셔너리

    # 모든 알파벳에 대해 우선 True로 저장
    # ord(문자) = 아스키코드
    # chr(아스키코드) = 문자
    ord_a = ord('A')
    for i in range(26):
        is_available[chr(i + ord_a)] = True

    idx = 0 # 화살표가 가르키는 인덱스

    for rot, alpha in record:
        idx = (idx - int(rot)) % n
        
        # 같은 경우
        if wheel[idx] == alpha:
            continue
        # 다른 알파벳이 써 있거나, 이미 알파벳을 다른 자리에 사용한 경우
        if wheel[idx] != '?' or not is_available[alpha]:
            return '!'
        wheel[idx] = alpha
        is_available[alpha] = False
                
    return ''.join(wheel[idx:]+wheel[:idx])

# 입력
n, k = map(int, input().split())
record = [input().split() for _ in range(k)]
    
print(make_wheel(n, record))
