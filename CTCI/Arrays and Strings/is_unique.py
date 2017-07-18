"""
1.1 - Implement an algorithm to determine if a string
has all unique characters. What if you cannot use any
additional data structures?
"""

def unique(word):
    """
    Returns 'True' if the given word has all
    unique characters and 'False' otherwise.
    """
    word = ''.join(word.split())    # assuming whitepsace is ignored
    chars = {}
    for char in word:
        count = chars.get(char, None)
        if count is None:
            chars[char] = 1
        else:
            return False
    return True

def unique_v2(word):    # no data structure
    """
    Returns 'True' if the given word has all
    unique characters and 'False' otherwise.
    """
    word = sorted(word)
    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            return False
    return True


# Unit Tests:
if __name__ == '__main__':
    assert(unique('allan') == False)
    assert(unique(' a l l a n') == False)
    assert(unique('') == True)
    assert(unique('strong') == True)
    assert(unique('a') == True)
    assert(unique('ctci      ') == False)
    assert(unique_v2('allan') == False)
    assert(unique_v2(' a l l a n') == False)
    assert(unique_v2('') == True)
    assert(unique_v2('strong') == True)
    assert(unique_v2('a') == True)
    assert(unique_v2('ctci      ') == False)

