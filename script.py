def add(a, b):
    return a + b


def division(a, b):
    if b == 0:
        raise ValueError("Zero division is not allowed")
    return a / b
