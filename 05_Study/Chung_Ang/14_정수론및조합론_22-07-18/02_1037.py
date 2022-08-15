'''
양수 A가 N의 진짜 약수가 되려면
N이 A의 배수이고, A가 1과 N이 아니어야한다.
어떤수 N의 진짜 약수가 주어질때 N을 구하는 프로그램
입력)
    - N의 진짜 약수의 개수
    - N의 진짜 약수가 주어진다.
32 비트 부호 있는 정수로 표현 가능????
'''
import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
nums.sort()
print(nums[0] * nums[-1])