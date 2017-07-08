"""
A look into recursive functions.
"""

# Example one:
def factorial(n):
    """Calculates n!"""
    if (n == 0):
        return 1
    return n * factorial(n-1)


# Example two:
def draw_line(length, label=''):
    """Draws a line with a given length and an optional label."""
    line = '-' * length
    if label:
        line += ' ' + label
    print(line)

def draw_interval(center_len):
    """Draws tick interval based upon a central tick length."""
    if center_len > 0:
        draw_interval(center_len - 1)
        draw_line(center_len)
        draw_interval(center_len - 1)


def draw_ruler(inches, major_len):
    """
    Draws an English ruler.

    inches      -> number of inches on the ruler
    major_len   -> length of the major tick
    """
    draw_line(major_len, '0')
    for i in range(1, inches + 1):
        draw_interval(major_len - 1)
        draw_line(major_len, str(i))


# Example three:
def binary_search(data, target, lo=None, hi=None):
    """
    Returns 'True' if target is found in data and 'False' otherwise.
    Assumes that the data is sorted.

    data    -> list of values
    target  -> desired value
    lo      -> index placeholder
    hi      -> index placeholder
    """
    if (lo == None) and (hi == None):   # for the lazy
        lo = 0
        hi = len(data) - 1

    if lo > hi:
        return False
    else:
        mid = (lo + hi) // 2
        if (data[mid] > target):
            return binary_search(data, target, lo, mid - 1)
        elif (data[mid] < target):
            return binary_search(data, target, mid + 1, hi)
        else:
            return True
    
