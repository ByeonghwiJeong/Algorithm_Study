'''
< 체육복 >
- 학생들의 번호는 체격순으로 메겨져 있어
- 바로 앞번호 뒷번호 학생에게만 체육복을 발려줄수 있습니다

전체학생수 n, 체육복은 도난당한 학생번호 배열 lost, 
여벌의 체육복을 가져온 번호 배열 reverse

수업을 들을수 잇는 학생의 최댓값
'''

def solution(n, lost, reserve):
    check = [0] * (n + 1)
    for v in lost: check[v] -= 1
    for v in reserve: check[v] += 1
    print(check)

    answer = 0
    return answer


print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5, [2, 4], [3]))