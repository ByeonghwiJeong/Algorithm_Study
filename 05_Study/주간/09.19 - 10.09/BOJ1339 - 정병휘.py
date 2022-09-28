"""
< 단어 수학 >
https://www.acmicpc.net/problem/1339

N개의 단어가 주어질때
대문자를 0 ~ 9까지의 숫자 중 하나로 바꿔서 N개의 수를 합하는 문제
알파벳은 같은 숫자로 바꿔야하며 두 개 이상의 알파벳이 같은 숫자로 바뀌어지면 안된다.

"""
N = int(input())
words = []
for _ in range(N):
    words.append(list(map(lambda x : ord(x) - 65, input())))

alphabets = [0] * 26 # 자릿수 저장
for w in words:
    for i, v in enumerate(w[::-1]):
        alphabets[v] += (10 ** i)
alphabets.sort(reverse=True)
sum_value = 0
num = 9
for i in range(9):
    sum_value += num * alphabets[i]
    num -= 1
print(sum_value)
'''
단어들을 우선 ord()함수를 사용해서 int형태의 리스트로 저장
alphabets ~ [0] * 26 자릿수저장하는 리스트선언
- 자릿수는 단어를 한번 reverse해줘야 그 인덱스를 기준으로 숫자를 부여할 수있음
- alphabets 내림차순정렬
결과
- 9부터 1씩내리면서 alphabets을 곱하면서 더하기
'''