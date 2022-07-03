'''
1. 시험점수 일부 조작해서 성적이 감소하지않는 형태로 만들려 합니다.

2. 감소하지 않는 형태란
 - 뒤점수 >= 앞쪽점수
3. 점수를 낮추는 방식으로만 조작

4. 각시험점수와 원래점수 차이의 합이 최소
'''
grade = list(map(int, input().split()))
grade.reverse()
print(grade)
answer = 0
for i in range(len(grade)-1):
    if grade[i] < grade[i+1]:
        answer += grade[i+1] - grade[i]
        grade[i+1] = grade[i]
        print(f'i: {i} // grade = {grade}')
print(answer)