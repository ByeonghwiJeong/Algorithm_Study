"""
?
https://school.programmers.co.kr/learn/courses/30/lessons/81302

! 접근)
* BFS로 푸는것이 아닌가???
    * -> 5x5행렬이므로 일부러 배열로 접근
* 1. 주어진 장소(places)의 정보를 받음
* 2. 문자열(string)을 문자(char)의 배열([])로 생각하여 2중 for문을 작성
* 3. 맨해튼 거리 2이하 & 파티션의 유무를 고려하여 거리두기를 검사
* 4. 결과값 반환

! 거리두기 안된경우)
* 1. 거리가 1인경우
* 2. 거리가 2이며 중간에 파티션이 없는경우(2가지 - 열, 행)
* 3. 거리가 2이며, 행/열이 모두 다르고 두 'P'의 사이에 파티션이 모두 없는 경우
PO
OP 왼쪽예시가 아닌경우

"""

def check(place):
    plist = [(r, c) for r in range(5) for c in range(5) if place[r][c] == 'P']

    for r1, c1 in plist:
        for r2, c2 in plist:
            dist = abs(r1 - r2) + abs(c1 - c2)
            if dist == 0 or dist > 2:
                continue 
            if dist == 1: return 0
            if r1 == r2 and place[r1][(c1+c2)//2] != 'X': return 0
            if c1 == c2 and place[(r1+r2)//2][c1] != 'X': return 0
            # if r1 != r2 and c1 != c2:
            #     if place[r1][c2] == 'X' and place[r2][c1] == 'X': return 1
            #     return 0
            if r1 != r2 and c1 != c2:
                if place[r1][c2] != 'X' or place[r2][c1] != 'X': return 0
    return 1

def solution(places):
    answer = [check(place) for place in places]
    return answer 
