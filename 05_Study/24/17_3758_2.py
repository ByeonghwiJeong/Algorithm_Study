'''
https://www.acmicpc.net/problem/3758
제목 : KCPC

문제)
- 대회에서 K개의 문제를 풀어야함
- 어떤 문제를 서버에 제출하면 0 ~ 100점을 받을 수 있음
- 풀이를 제출한 팀의 ID, 문제 번호, 점수가 시간순서대로 저장
- 한 문제데 대한 풀이를 여러번 제출할 수 있음 (최고 점수가 최종점수)
- 팀의 최종 점수 : 각 문제에 대한 최종 점수의 합
- 팀의 순위 : (높은 점수를 받은 팀의 수) + 1
- 점수가 동일한 팀이 있는경우
  1. 최종 점수가 같은 경우 - 풀이를 제출한 횟수가 적은 팀의 순위가 높음
  2. 최종 점수도 같고 제출 횟수도 같은 경우, 마지막 제출 시간이 더 빠른 팀의 순위가 높음
    (동시 제출 시간은 없음)
- 서버의 로그가 주어질때, 당신 팀의 순위를 계산하는 프로그램을 작성

입력)
- 1 : 테스트 케이스의 수 T ~ [1, 100]
- 2 : 팀의 수 n, 문제의 개수 k, 당신 팀의 ID t, 서버의 로그의 개수 m
     n, k ~ [3, 100], t ~ [1, n], m ~ [3, 10000]
- 3 : (m lines)
    - i, j, s : i번 팀이 j번 문제에 s점을 받음
    - i ~ [1, n]
    - j ~ [1, k]
    - s ~ [0, 100]
'''
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n, k, t, m = map(int, input().split())

    # 각 팀의 문제별 점수, 제출 횟수, 마지막 제출 시간 관리를 위한 딕셔너리 초기화
    team_dict = {
        i: {
            'scores': [0] * (k+1),  # 문제 번호 1 ~ k, 0번 인덱스는 사용하지 않음
            'submit_cnt': 0,        # 제출 횟수
            'last_submit_time': 0   # 마지막 제출 시간
        }
        for i in range(1, n+1)
    }

    # 로그 처리
    for idx in range(m):
        i, j, s = map(int, input().split())
        team_dict[i]['scores'][j] = max(team_dict[i]['scores'][j], s)
        team_dict[i]['submit_cnt'] += 1
        team_dict[i]['last_submit_time'] = idx

    # 팀을 정렬
    sorted_team = sorted(
        team_dict.keys(),
        key=lambda x: (
            -sum(team_dict[x]['scores']),       # 총 점수의 내림차순
            team_dict[x]['submit_cnt'],         # 제출 횟수의 오름차순
            team_dict[x]['last_submit_time']    # 마지막 제출 시간의 오름차순
        )
    )

    # 당신 팀의 순위 출력
    print(sorted_team.index(t) + 1)

