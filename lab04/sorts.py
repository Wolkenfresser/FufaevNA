"""
Три базовых алгоритма сортировки.
Уровень: 3.
Содержит:
- bubble_sort
- selection_sort
- insertion_sort
Каждый алгоритм содержит комментарии с оценкой сложности.
"""

# Сортировка пузырьком (Bubble Sort)
# Время: O(n^2) в худшем, среднем и лучшем (уже отсортированном) случаях.
# Память: O(1)

def bubble_sort(arr):
    a = arr.copy()
    n = len(a)
    for i in range(n):
        for j in range(0, n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


# Сортировка выбором (Selection Sort)
# Время: O(n^2) во всех случаях.
# Память: O(1)

def selection_sort(arr):
    a = arr.copy()
    n = len(a)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if a[j] < a[min_index]:
                min_index = j
        a[i], a[min_index] = a[min_index], a[i]
    return a


# Сортировка вставками (Insertion Sort)
# Время: лучш. — O(n), сред./худш. — O(n^2).
# Память: O(1)

def insertion_sort(arr):
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


if __name__ == "__main__":
    data = [5, 3, 8, 4, 2]
    print("Bubble:", bubble_sort(data))
    print("Selection:", selection_sort(data))
    print("Insertion:", insertion_sort(data))