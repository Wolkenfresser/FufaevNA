"""
task_solutions.py
Практическая задача: проверка сбалансированности скобок с помощью стека (list).
"""

BRACKETS = {
    ')': '(',
    ']': '[',
    '}': '{'
}


def is_balanced(s: str) -> bool:
    stack = []  # стек, реализованный на list
    for ch in s:
        if ch in '([{':
            stack.append(ch)  # push — O(1)
        elif ch in ')]}':
            if not stack:
                return False
            if stack.pop() != BRACKETS[ch]:  # pop — O(1)
                return False
        # игнорируем другие символы
    return not stack


if __name__ == '__main__':
    tests = [
        ("([]){}", True),
        ("([)]", False),
        ("((()))", True),
        ("", True),
        ("{[()()]}", True)
    ]
    for s, expected in tests:
        print(s, is_balanced(s), "expected=", expected)