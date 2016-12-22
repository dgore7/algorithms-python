def make_change_td(coins, money):
    return make_change_helper(coins, money, 0)


def make_change_helper(coins, money, index):
    if money == 0:
        return 1
    if index >= len(coins):
        return 0
    ways = 0
    iter = 0
    while iter * coins[index] <= money:
        ways += make_change_helper(coins, money - iter * coins[index], index + 1)
        iter += 1
    return ways

import sys

def make_change_bu(coins, money):
    solution_table = [0 for i in range(money + 1)]
    solution_table[0] = 1
    for coin in coins:
        for j in range(coin, money+1):
            solution_table[j] += solution_table[j - coin]
    return solution_table[money]

if __name__ == '__main__':
    print(make_change_td([2, 5, 3, 6], 10))
    print(make_change_bu([1, 2, 3], 4))

#    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
#    [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 2]
#    [1, 0, 1, 1, 1, 2, 2, 2, 3, 3,]