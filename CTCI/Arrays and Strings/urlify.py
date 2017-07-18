"""
1.3 - Write a method to replace all spaces in a string
with '%20'. You may assume that the string has sufficient
space at the end to hold the additional characters, and
that you are given the true length of the string.
"""

def urlify(string):
    string = string.strip()
    string = list(string)
    for i in range(len(string)):
        if (string[i] == ' '):
            string[i] = '%20'
    return ''.join(string)


# Unit Tests:
if __name__ == '__main__':
    assert(urlify('test') == 'test')
    assert(urlify('testing my function') == 'testing%20my%20function')
    assert(urlify('') == '')
    assert(urlify(' ') == '')
    assert(urlify('      a ll a n         ') == 'a%20ll%20a%20n')
