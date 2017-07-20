"""
1.9 - Assume you have a method which checks if one word is
a substring of another. Given two strings, s1 and s2, write
code to check if s2 is a rotation of s1 using only one call
to this method (ex: "waterbottle" is a rotation of "erbottlewat").
"""

def string_rotation(str1, str2):
    if str2 == '':
        return True
    try:
        index = str2.index(str1[0])
    except:
        return False
    str2 = str2[index:] + str2[:index]
    return str2 in str1


# Unit Tests:
if __name__ == '__main__':
    assert(string_rotation('waterbottle', 'erbottlewat') == True)
    assert(string_rotation('erbottlewat', 'waterbottle') == True)
    assert(string_rotation('animal', 'plant') == False)
    assert(string_rotation('', '') == True)
    assert(string_rotation('allan', '') == True)
    assert(string_rotation('milk', 'ilkm') == True)

