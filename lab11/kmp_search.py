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
