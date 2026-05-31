def min_path(grid):
    if not grid or not grid[0]:
        return 0
    m = len(grid)
    n = len(grid[0])
    dp = [0] * n
    dp[0] = grid[0][0]
    # заполняем только вправо
    for j in range(1, n):
        dp[j] = dp[j - 1] + grid[0][j]
    for i in range(1, m):
        # вниз
        dp[0] += grid[i][0]
        for j in range(1, n):
            # Выбираем минимум между верхней и нижней
            dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]
    return dp[-1]
matrix = [
    [1, 3, 4],
    [1, 5, 1],
    [4, 2, 1]
]
print(f"минимальный путь: {min_path(matrix)}")

