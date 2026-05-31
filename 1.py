def marshrut(n):
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 1
    dp[3] = 2
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n == 3:
        return 2
    for i in range(4, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    return dp[n]

n = 25
print(f"Количество маршрутов до {n} камня: {marshrut(n)}")
