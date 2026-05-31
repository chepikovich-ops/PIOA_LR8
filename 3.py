def coin_change(coins, amount):
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount] if dp[amount] <= amount else -1

coins = [1, 2, 5]
S = 121
print(f"минимальное кол-во монет для {S}: {coin_change(coins, S)}")

coins_2 = [2]
S_2 = 3
print(f"минимальное количество монет для {S_2}: {coin_change(coins_2, S_2)}")
