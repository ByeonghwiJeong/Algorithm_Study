"""
< string Chains >
Given an array of words representing
"""

def longestChain(words):
    # Write your code here
    _dict = {w: 1 for w in words}
    words.sort(key=len)
    for word in words:
        for i in range(len(word)):
            s = word[:i] + word[i + 1 :]
            if s in _dict:
                if _dict[s] + 1 > _dict[word]:  # 추가
                    _dict[word] = _dict[s] + 1
    return max(_dict.values())
