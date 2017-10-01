coins = [200, 100, 25, 10, 5, 1] # Canadian denominations

def change_greedy(n):
    if (n == 0):
        return 0
    for coin in coins:
        if ((n - coin) >= 0):
            min_coins = change_greedy(n - coin)
            return min_coins + 1

def change_naive(n):
    if (n == 0):
        return 0
    min_coins = float('inf')
    for coin in coins:
        if ((n - coin) >= 0):
            curmin = change_naive(n - coin)
            if (curmin < min_coins):
                min_coins = curmin
    return min_coins + 1

def change_dp1(n): # Top-down solution
    cache = {0: 0}
    return _change(n, cache)

def _change(n, cache):
    if (n in cache):
        return cache[n]
    min_coins = float('inf')
    for coin in coins:
        if ((n - coin) >= 0):
            curmin = _change(n - coin, cache)
            if (curmin < min_coins):
                min_coins = curmin
                cache[n] = curmin + 1
    return cache.get(n, 0)

def change_dp2(n): # Bottom-up solution
    cache = {}
    for i in range(1, n+1):
        min_coins = float('inf')
        for coin in coins:
            if ((i - coin) >= 0):
                curmin = cache.get(i - coin, 0) + 1
                if curmin < min_coins:
                    min_coins = curmin
                    cache[i] = min_coins
    return cache[n]

# Unit Tests:
if __name__ == '__main__':
    assert(change_greedy(1) == 1)
    assert(change_greedy(6) == 2)
    assert(change_greedy(49) == 7)
    assert(change_greedy(100) == 1)
    assert(change_greedy(149) == 8)
    assert(change_greedy(300) == 2)
    assert(change_naive(1) == 1)
    assert(change_naive(6) == 2)
    assert(change_naive(49) == 7)
    assert(change_dp1(1) == 1)
    assert(change_dp1(6) == 2)
    assert(change_dp1(49) == 7)
    assert(change_dp1(100) == 1)
    assert(change_dp1(149) == 8)
    assert(change_dp1(300) == 2)
    assert(change_dp2(1) == 1)
    assert(change_dp2(6) == 2)
    assert(change_dp2(49) == 7)
    assert(change_dp2(100) == 1)
    assert(change_dp2(149) == 8)
    assert(change_dp2(300) == 2)
