# dynamic programing
# divide the problem into sub problems
# find the minimum compination of coins for the given amount
# use non recursive bottom-up approch

# generate  the complete coin combinations for the individual small amounts
# that is for amount 10 in [0, 1, 2, ... 10]
# then find the minimum coins needed
def min_coin_problem(coins, amount):
    result = []
    w = amount + 1
    coins_len = len(coins)
    for i in range(coins_len):
        temp = []
        for j in range(w):
            if j == 0:
                temp.append(0)
            else:
                if coins[i] > j:
                    temp.append(result[i-1][j])
                else:
                    if i == 0:
                        temp.append(1+temp[j-coins[i]])
                    else:
                        temp.append(min(result[i-1][j], 1+temp[j-coins[i]]))
        result.append(temp)
    number_of_coins = result[coins_len-1][amount]
    coins_list = find_the_coin_combinations(result, coins, amount)
    return number_of_coins, coins_list

# find the which coins used for the amount with minimum numbers
def find_the_coin_combinations(conins_comp, coins, amount):
    i = len(coins) - 1
    j = amount
    k = i - 1
    min_coin_list = list() 
    amount_list = list(i for i in range(amount + 1))
    while True:
        if conins_comp[i][j] == conins_comp[k][j]:
            i = k
            k = k - 1
        else:
            min_coin_list.append(coins[i])
            j = amount_list[j] - coins[i]
            k = i - 1

        if conins_comp[i][j] == 0:
            break

    return min_coin_list




if __name__ == "__main__":
    amount = 10
    coins = [1, 5, 6, 9]
    min_coins, coin_combinations = min_coin_problem(coins, amount)
    print('The minimum number of coin need for the amount', amount, 'is', min_coins, 'coins')
    print('The coin combination for the amount', amount, 'is', coin_combinations)