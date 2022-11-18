from collections import Counter

def solution(movies):
    c = Counter(movies)
    c = c.most_common()
    c.sort(key=lambda x: (-x[1], x[0]))
    answer = [x[0] for x in c]
    return answer

print(solution(['spy', 'ray', 'spy', 'room', 'once', 'ray', 'spy', 'once']))
# ['spy', 'once', 'ray', 'room']