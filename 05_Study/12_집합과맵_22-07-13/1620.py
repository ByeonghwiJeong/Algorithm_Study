'''
입력 N, M
N - 포켓몬이름
M - 체크할이름 or 번호
    출력 이름 <---> 번호 
'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
name_dict = dict()
num_dict = dict()
for i in range(1, N + 1):
    _input = input().rstrip()
    name_dict[_input] = i
    num_dict[i] = _input
for _ in range(M):
    _input = input().rstrip()
    if _input.isdigit():
        _input = int(_input)
        print(num_dict[_input]) 
    else:
        print(name_dict[_input])
