'''
https://www.acmicpc.net/problem/9017

제목 : 크로스 컨트리

문제)
- 한팀은 여섯 명의 선수로 구헝
- 팀 점수는 사우이 네 명의 점수의 합
- 잠수는 자격을 갖춘 팀의 주자들에게만 주어짐
- 가장 낮은 점수를 얻는 팀이 우승
- 여섯 명의 주자가 참가하지 못한 팀은 점수 계산 제외
- 동점의 경우 : 다섯 번째 주자가 가장 빨리 들어온 팀이 우승
- 우승팀을 출력

입력)
- 1 : T (테스트 케이스)
- 2 : N (사람의 수) ~ [2, 100]
- 3 : N개의 팀 번호
'''

import sys
from collections import defaultdict
input = sys.stdin.readline



for _ in range(int(input())):
    N = int(input())
    team = list(map(int, input().split()))
    team_dict = defaultdict(int)
    for t in team:
        team_dict[t] += 1
    under_6 = [k for k, v in team_dict.items() if v < 6]

    cnt = 1
    team_score = defaultdict(int)
    team_cnt = defaultdict(int)
    team_5th = defaultdict(int)
    for i, t in enumerate(team):
        if t in under_6:
            continue
        if team_cnt[t] < 4:
            team_score[t] += cnt
            cnt += 1
            team_cnt[t] += 1
        elif team_cnt[t] == 4:
            team_5th[t] = cnt
            team_cnt[t] += 1
            cnt += 1
        else:
            cnt += 1

    # 가장 점수 낮은 팀 하나 출력 , 동점자 있으면 team_5th[t]가 작은 팀 출력
    min_score = min(team_score.values())
    min_team = [k for k, v in team_score.items() if v == min_score]
    if len(min_team) == 1:
        print(min_team[0])
    else:
        min_5th = min([team_5th[t] for t in min_team])
        print([k for k, v in team_5th.items() if v == min_5th][0])


    # print(team_score)
    # print(team_cnt)
    # print(team_5th)



