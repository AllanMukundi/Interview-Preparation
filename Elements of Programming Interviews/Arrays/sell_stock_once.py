def sell_stock_once(prices):
    curmin, profit = float('inf'), 0
    for price in prices:
        curmin = min(price, curmin)
        profit = max(price-curmin, profit)
    return profit

# Unit Tests:
if __name__ == '__main__':
    assert(sell_stock_once([310, 315, 275, 295, 260, 270, 290, 230, 255, 250]) == 30)
    assert(sell_stock_once([10] * 6) == 0)
    assert(sell_stock_once([10, 20, 30]) == 20)
    assert(sell_stock_once([30, 20, 10]) == 0)
    assert(sell_stock_once([40, 19, 40, 2, 18, 51, 19, 33, -5, 40]) == 49)
    assert(sell_stock_once([float('-inf'), float('inf')]) == float('inf'))
    assert(sell_stock_once([-20, -30, -40, -50, -80, -19, 0]) ==  80)
