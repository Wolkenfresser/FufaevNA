def prefix_function(s):
    """
    Вычисляет префикс-функцию строки s.
    Сложность: O(n)
    """
    n = len(s)
    pi = [0] * n
    j = 0

    for i in range(1, n):
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j

    return pi