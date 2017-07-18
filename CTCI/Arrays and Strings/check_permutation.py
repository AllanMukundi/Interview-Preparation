from collections import Counter

"""
1.2 - Given two strings, write a method to decide if 
one is a permutation of the other.
"""

def is_permutation(str1, str2):
    if (len(str1) != len(str2)):
        return False
    else:
        str1 = sorted(str1)
        str2 = sorted(str2)
        return (str1 == str2)

def is_permutation_v2(str1, str2):
    if (len(str1) != len(str2)):
        return False
    else:
        count = Counter()
        for char in str1:
            count[char] += 1
        for char in str2:
            if (count[char] == 0):
                return False
            count[char] -= 1
        return True


# Unit Tests:
if __name__ == '__main__':
    assert(is_permutation('', '') == True)
    assert(is_permutation('', 'a') == False)
    assert(is_permutation('a', '') == False)
    assert(is_permutation('a', 'a') == True)
    assert(is_permutation('animal', 'lanima') == True)
    assert(is_permutation('banana', 'bananas') == False)

