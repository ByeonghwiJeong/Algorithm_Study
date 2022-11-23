from collections import Counter
# 
def solution(movies):
    c = Counter(movies)
    c = c.most_common()
    c.sort(key=lambda x: (-x[1], x[0]))
    answer = [x[0] for x in c] # list comprehension
    return answer

def solution2(movies):
    c = dict()
    for movie in movies:
        if movie in c:
            c[movie] += 1
        else: c[movie] = 1
    c = list(c.items())
    c.sort(key=lambda x: (-x[1], x[0]))
    

print(solution(['spy', 'ray', 'spy', 'room', 'once', 'ray', 'spy', 'once']))
# ['spy', 'once', 'ray', 'room']


'''
>>> a = ['spy', 'ray', 'spy', 'room', 'once', 'ray', 'spy', 'once']
>>> a
['spy', 'ray', 'spy', 'room', 'once', 'ray', 'spy', 'once']
>>> from collections import Counter
>>> b = Counter(a)
>>> b
Counter({'spy': 3, 'ray': 2, 'once': 2, 'room': 1})
[('spy', 3), ('once', 2), ('ray', 2), ('room', 1)]
>>> [x[1] for x in c]
[3, 2, 2, 1]
>>> [x[0] for x in c]
['spy', 'once', 'ray', 'room']
'''