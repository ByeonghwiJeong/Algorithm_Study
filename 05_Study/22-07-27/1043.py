'''
지민이는 사실 or 거짓
그 이야기의 진실을 아는 사람들이 있다.
그런 사람이 있는경우 사실로 말한다.

어떤사람이 진실을 듣고
다른 파티에서 거짓을 들을경우 
지민이는 거짓말쟁이가 된다.

사람의 수 N
그 이야기의 진실을 아는 사람이 주어진다.
각 파티에 오는 사람들의 번호가 주어진다.
지민이는 모든 파티에 참가해야한다.

지민이가 거짓말쟁이로 알려지지 않으면서
과장된 이야기를 할 수 있는 파티 개수 최대값

입력)
    - 사람수N 파티의수M 
    - 이야기의 진실을 아는 사람 수와 번호
    - 3째줄부터 M개의 줄
        - 각 파티마다 오는 사람의 수 & 번호
- N, M은 50 이하의 자연수
- 진실을 아는 사람의 수는  0 ~ 50
- 각 파티마다 오는 사람의 수는 1 ~ 50
출력)
    - 정답

내생각
- 진실을 아는 사람이 참여한 파티의 인원

5 4
1 4 > 5
1 3 4 > t
2 2 3 > t
3 1 2 > t
4 5 1 > t       


'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
tnum, *_true = map(int, input().split())
_true = set(_true)
parties = []
for _ in range(M):
    pnum, *_party = map(int, input().split())
    parties.append(set(_party))

print(parties)