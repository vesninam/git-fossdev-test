def add(a, b):
    return a + b


def division(a, b):
    if b == 0:
        raise ValueError("Zero division is not allowed")
    if isinstance(a, str) or isinstance(b, str):
        raise ValueError("String division is not allowed")
    return a / b
