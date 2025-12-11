"""
Два жадных алгоритма (уровень 3):
1) Interval Scheduling
2) Fractional Knapsack
Каждый алгоритм содержит комментарии со сложностью.
"""

# ---------------------------------------------------------
# 1. Выбор заявок (Interval Scheduling)
# Жадный выбор: сортировать интервалы по времени окончания
# Сложность: O(n log n)
# ---------------------------------------------------------

def interval_scheduling(intervals):
    # intervals = [(start, end), ...]
    intervals = sorted(intervals, key=lambda x: x[1])  # сортировка по окончанию
    result = []
    current_end = -float('inf')

    for start, end in intervals:
        if start >= current_end:
            result.append((start, end))
            current_end = end

    return result


# ---------------------------------------------------------
# 2. Непрерывный рюкзак (Fractional Knapsack)
# Жадный выбор: брать предметы с максимальной удельной стоимостью (value/weight)
# Сложность: O(n log n) — сортировка
# ---------------------------------------------------------

def fractional_knapsack(items, capacity):
    # items = [(value, weight), ...]
    # сортировка по value/weight
    items = sorted(items, key=lambda x: x[0] / x[1], reverse=True)

    total_value = 0
    remaining = capacity

    for value, weight in items:
        if remaining == 0:
            break
        if weight <= remaining:
            total_value += value
            remaining -= weight
        else:
            fraction = remaining / weight
            total_value += value * fraction
            remaining = 0
            break

    return total_value


if __name__ == "__main__":
    # Демонстрация
    intervals = [(1, 3), (2, 5), (4, 7), (1, 8), (5, 9)]
    print("Interval Scheduling ->", interval_scheduling(intervals))

    items = [(60, 10), (100, 20), (120, 30)]
    print("Fractional knapsack ->", fractional_knapsack(items, 50))