"""
1.6 - Implement a method to perform basic string compression using
the counts of repeated characters. For example, the string
'aabcccccaaa' would become 'a2b1c5a3'.
"""

def compress(word):
    compressed = ''
    i = 0
    while (i < len(word)):
        walk = i+1
        while (walk < len(word)):
            if (word[i] == word[walk]):
                walk += 1
            else:
                break
        compressed += word[i] + str(walk-i)
        i += (walk - i)
    return compressed if len(compressed) < len(word) else word


# Unit Tests:
if __name__ == '__main__':
    assert(compress('aabcccccaaa') == 'a2b1c5a3')
    assert(compress('dog') == 'dog')
    assert(compress('allan') == 'allan')
    assert(compress('alllan') == 'alllan')
    assert(compress('allllan') == 'allllan')
    assert(compress('allllllan') == 'a1l6a1n1')
    assert(compress('') == '')
    assert(compress('aAbCcCcCaAa') == 'aAbCcCcCaAa')
    assert(compress('AAbCCCCcaaa') == 'A2b1C4c1a3')

