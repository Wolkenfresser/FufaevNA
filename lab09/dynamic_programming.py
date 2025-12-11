"""
Динамическое программирование (базовый набор для оценки 3)
1) Фибоначчи — табличный DP
2) 0–1 Knapsack — bottom-up DP
Каждый алгоритм содержит пояснение и сложность.
"""

# ---------------------------------------------
# 1. Числа Фибоначчи — bottom-up (итеративное DP)
# Время: O(n), Память: O(n)
# ---------------------------------------------

def fib_dp(n: int) -> int:
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


# ---------------------------------------------
# 2. 0–1 Knapsack — bottom-up DP
# Время: O(n * W), Память: O(n * W)
# items = [(value, weight), ...]
# ---------------------------------------------

def knapsack_01(items, capacity):
    n = len(items)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        value, weight = items[i - 1]
        for w in range(capacity + 1):
            if weight <= w:
                dp[i][w] = max(
                    dp[i - 1][w],  # не берём
                    dp[i - 1][w - weight] + value  # берём
                )
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[n][capacity]


if __name__ == "__main__":
    print("fib_dp(10) =", fib_dp(10))
    items = [(60, 10), (100, 20), (120, 30)]
    print("knapsack =", knapsack_01(items, 50))