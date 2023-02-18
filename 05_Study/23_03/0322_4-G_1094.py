'''
< 막대기 >
https://www.acmicpc.net/problem/1094
문제)
- 길이가 64cm인 막대기
- Xcm인 막대를 가지고 싶다.
- 아래와 같은 방법으로 막대를 자르려고 한다.
    - 1. 지민이가 가지고있는 막대의 길이를 모두 더한다.
    - 2. 합이 X보다 크다면 아래와 같은과정을 반복
        - 가지고 있는 막대 중 길이가 가장 짧은 것을 절반으로 자른다.
        - 자른 막대의 절반중 하나를 버리고 남은 길이의 합이 X보다 크면 

입력)
- 1     :  
출력)
- 1     : 
'''
import sys
input = sys.stdin.readline

print(bin(int(input())).count('1'))

# print(int(input()).bit_count())