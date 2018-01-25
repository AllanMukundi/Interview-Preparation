def int_to_str(num):
    negative = True if num < 0 else False
    num = abs(num)
    string = []
    while(True):
        string.append(chr(ord('0') + (num % 10)))
        num //= 10
        if (num == 0): break
    return '-' + ''.join(reversed(string)) if negative else ''.join(reversed(string))

def str_to_int(string):
    negative = True if string[0] == '-' else False
    string = string[1:] if negative else string
    digits = list(map(lambda x: ord(x) - ord('0'), list(string)))
    num = 0
    for i in range(len(digits)):
        num = (num * 10) + digits[i]
    return (-1 * num) if negative else num

# Unit Tests:
if __name__ == '__main__':
    assert(int_to_str(15) == '15')
    assert(int_to_str(0) == '0')
    assert(int_to_str(512) == '512')
    assert(int_to_str(-0) == '0')
    assert(int_to_str(-10) == '-10')
    assert(int_to_str(-3192) == '-3192')
    assert(int_to_str(1231) == '1231')
    assert(str_to_int('15') == 15)
    assert(str_to_int('0') == 0)
    assert(str_to_int('512') == 512)
    assert(str_to_int('-0') == 0)
    assert(str_to_int('-10') == -10)
    assert(str_to_int('-3192') == -3192)
    assert(str_to_int('1231') == 1231)
