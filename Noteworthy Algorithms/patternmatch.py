"""
A collection of string-matching algorithms which 
determine if a pattern is present in some string.
"""

def find_brute(word, pattern):
    """
    Returns the lowest index of word in which the specified
    pattern begins (or -1 if no such pattern exists).
    """
    word_len, pattern_len = len(word), len(pattern)
    for i in range(word_len - pattern_len + 1):
        k = 0
        while (k < pattern_len and word[i+k] == pattern[k]):
            k += 1
        if (k == pattern_len):
            return i
    return -1

def find_boyer_moore(word, pattern):
    """
    Returns the lowest index of word in which the specified
    pattern begins (or -1 if no such pattern exists).
    """
    w_len, p_len = len(word), len(pattern)
    if (p_len == 0):
        return 0
    last = {}
    for n in range(p_len):
        last[pattern[n]] = n
    i = j = p_len - 1
    while (i < w_len):
        if (word[i] == pattern[j]):
            if (j == 0):
                return i
            else:
                i -= 1
                j -= 1
        else:
            k = last.get(word[i], -1)
            i += p_len - min(k+1, j)
            j = p_len - 1
    return -1

# Unit Tests:
if __name__ == '__main__':
    assert(find_brute('this is my string', '') == 0)
    assert(find_brute('test', 'test') == 0)
    assert(find_brute('waterloo', 'loo') == 5)
    assert(find_brute('waterloo', 'cat') == -1)
    assert(find_brute('summer', 'm') == 2)
    assert(find_brute('t', 't') == 0)
    assert(find_brute('daniel', '') == 0)
    assert(find_brute('', 'testing') == -1)
    assert(find_brute('', '') == 0)
    assert(find_boyer_moore('this is my string', '') == 0)
    assert(find_boyer_moore('test', 'test') == 0)
    assert(find_boyer_moore('waterloo', 'loo') == 5)
    assert(find_boyer_moore('waterloo', 'cat') == -1)
    assert(find_boyer_moore('summer', 'm') == 2)
    assert(find_boyer_moore('caesar', '') == 0)
    assert(find_boyer_moore('t', 't') == 0)
    assert(find_boyer_moore('', 'testing') == -1)
    assert(find_boyer_moore('', '',) == 0)

