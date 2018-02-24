from collections import Counter

def is_constructible(letter, magazine):
    letter_c, magazine_c = Counter(letter), Counter(magazine)
    return len(letter_c - magazine_c) == 0


# Unit Tests:
if __name__ == '__main__':
    assert(is_constructible('', '') == True)
    assert(is_constructible('', 'allan') == True)
    assert(is_constructible('alan', 'allan') == True)
    assert(is_constructible('allan', 'alan') == False)
    assert(is_constructible('baboon', 'aabbccddeeffgghhiijjkkllmmnnooo') == True)
    assert(is_constructible('racecar', 'racecar') == True)
    assert(is_constructible('edmond', 'dantes') == False)
    assert(is_constructible('villefort', '') == False)
