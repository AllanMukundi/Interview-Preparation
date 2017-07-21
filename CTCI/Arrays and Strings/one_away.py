"""
1.5 - There are three types of edits that can be
performed on strings: inserting, removing, or replacing
a character. Given two strings, write a function to check
if they are zero or one edits away from each other.
"""

def one_edit(str1, str2):
    if abs(len(str1) - len(str2)) > 1:
        return False
    shorter = str1 if len(str1) < len(str2) else str2
    longer = str2 if shorter is str1 else str1
    edits = i = j = 0
    if (len(shorter) == len(longer)):
        while(i < len(longer)):
            if (shorter[i] != longer[j]):
                edits += 1
            i += 1
            j += 1
    else:
        while(i < len(shorter) and edits < 2):
            if (shorter[i] == longer[j]):
                i += 1
                j += 1
            else:
                j += 1
                edits += 1
    return (edits <= 1)


# Unit Tests:
if __name__ == '__main__':
    assert(one_edit('', '') == True)
    assert(one_edit('x', '') == True)
    assert(one_edit('pale', 'ple') == True)
    assert(one_edit('pales', 'pale') == True)
    assert(one_edit('pale', 'bale') == True)
    assert(one_edit('pale', 'bake') == False)
    assert(one_edit('allan', 'allan') == True)
    assert(one_edit('allan', 'alan') == True)
    assert(one_edit('allan', 'alen') == False)
    assert(one_edit('allan', 'foobarfoobar') == False)

