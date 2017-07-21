from collections import Counter

"""
1.4 - Given a string, write a function to check if it
is a permutation of a palindrome. The palindrome does
not need to be limited to just dictionary words.
"""

def clean(word):
    cleaned = ""
    for char in word:
        if ord('A') <= ord(char) <= ord('Z') or ord('a') <= ord(char) <= ord('z'):
            cleaned += char
    return cleaned

def palindrome_permutation(word):
    count = Counter()
    for char in clean(word):
        count[char] += 1
    return sum((num % 2) for num in count.values()) <= 1


# Unit Tests:
if __name__ == '__main__':
    assert(palindrome_permutation('') == True)
    assert(palindrome_permutation('a') == True)
    assert(palindrome_permutation('aa') == True)
    assert(palindrome_permutation('ab') == False)
    assert(palindrome_permutation('taco          cat') == True)
    assert(palindrome_permutation('racecar') == True)
    assert(palindrome_permutation('racecair') == False)

