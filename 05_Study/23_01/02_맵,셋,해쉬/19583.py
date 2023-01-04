'''
< 싸이버개강총회 >
문제)
- 온라인 스트리밍 문제 - 개강
    - 누가 왔는지 알 수 없다.
    - 끝까지 남은 사람 알 수 없다.
    - 틀어 놓기만 했는지 알 수 없다.
- 위 문제을 해결하기 위해서 출석부 관리
    - 1 : 개강 시작전 ~ 시작: 채팅O -> 입장확인
    - 2 : 개강 총회 끝나고 ~ : 채티얘 -> 퇴장확인
입력)
- 1     : 총회시작시각S, 총회끝난시각E, 스트리밍종료Q
    (00:00 ≤ S < E < Q ≤ 23:59)
- 2     : 
'''
import sys
input = sys.stdin.readline
S, E, Q = map(lambda x: int(x[:2] + x[3:]) ,input().split())

attend = set()
ans = 0
while True:
    try:
        time, name = input().split()
        time = int(time[:2] + time[3:])
        if time <= S:
            attend.add(name)
        elif E <= time <= Q:
            if name in attend:
                ans += 1
                attend.remove(name) # 중요 : 중복 체크 방지
    except:
        print(ans)
        break