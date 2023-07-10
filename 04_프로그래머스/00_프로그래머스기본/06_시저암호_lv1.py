"""
?
https://school.programmers.co.kr/learn/courses/30/lessons/64065


"""

def solution(s, n):
    answer = ""
    for i in s:
        if i == " ": answer += " "; continue
        st = ord('A') if i.isupper() else ord('a')
        answer += chr((ord(i) - st + n) % 26 + st)
    return answer