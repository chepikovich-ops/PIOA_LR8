def bag(weights, values, W):
    n = len(weights)
    dp = [0] * (W + 1)
    for i in range(n):
        w_item = weights[i]
        v_item = values[i]
        for w in range(W, w_item - 1, -1):
            dp[w] = max(dp[w], dp[w - w_item] + v_item)
    return dp[W]

weights = [20, 30, 40, 10]
values = [100, 30, 70,70]
W = 50
max_value = bag(weights, values, W)
print(f"максимальная ценность в рюкзаке: {max_value}")
