def fibonacci_naive(n):
    if (n == 0):
        return 0 
    elif (n == 1):
        return 1
    else:
        return fibonacci_naive(n-1) + fibonacci_naive(n-2)

def fibonacci_dp1(n): # Top-down solution
    cache = {0: 0, 1: 1}
    return _fibonacci(n, cache)

def _fibonacci(n, cache):
    if n in cache:
        return cache[n]
    else:
        cache[n] = _fibonacci(n-1, cache) + _fibonacci(n-2, cache)
        return cache[n]

def fibonacci_dp2(n): # Bottom-up solution
    cache = {0: 0, 1: 1}
    for i in range(2, n+1):
        cache[i] = cache[i-1] + cache[i-2]
    return cache[n]

# Unit Tests:
if __name__ == '__main__':
    assert(fibonacci_naive(0) == 0)
    assert(fibonacci_naive(1) == 1)
    assert(fibonacci_naive(5) == 5)
    assert(fibonacci_naive(10) == 55)
    assert(fibonacci_dp1(0) == 0)
    assert(fibonacci_dp1(1) == 1)
    assert(fibonacci_dp1(5) == 5)
    assert(fibonacci_dp1(10) == 55)
    assert(fibonacci_dp2(0) == 0)
    assert(fibonacci_dp2(1) == 1)
    assert(fibonacci_dp2(5) == 5)
    assert(fibonacci_dp2(10) == 55)

