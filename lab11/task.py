import time
import random
import string

def kmp_search(text, pattern):
    """
    Ищет все вхождения pattern в text.
    Сложность: O(n + m)
    """
    if not pattern:
        return []

    combined = pattern + "#" + text
    pi = prefix_function(combined)

    m = len(pattern)
    result = []

    for i in range(m + 1, len(combined)):
        if pi[i] == m:
            result.append(i - 2*m)

    return result

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

text = "".join(random.choice(string.ascii_lowercase) for _ in range(200000))
pattern = "abc"

# KMP
start = time.time()
kmp_search(text, pattern)
kmp_time = time.time() - start

# Префикс-функция сама по себе
start = time.time()
prefix_function(text)
pi_time = time.time() - start

print("Время KMP:", kmp_time)
print("Время префикс-функции:", pi_time)
