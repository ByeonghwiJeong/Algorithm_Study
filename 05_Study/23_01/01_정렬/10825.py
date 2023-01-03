'''
<  국영수 > 
https://www.acmicpc.net/problem/10825
문제)
- 국어, 영어, 수학 점수가 주어졌을 때, 정렬하는 플로그램을 작성하시오.
1. 국어 점수가 감소하는 순서로
2. 국어 점수가 같으면 영어 점수가 증가하는 순서로
3. 국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서로
4. 모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로

'''
import sys
input = sys.stdin.readline

N = int(input())
students = []
for _ in range(N):
    name, kor, eng, math = input().split()
    students.append([name, int(kor), int(eng), int(math)])

students.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))
for student in students:
    print(student[0])

    