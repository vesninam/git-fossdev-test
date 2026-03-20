from script import add, division

def test_addition():
    assert add(1, 2) == 3
    print("Test addition passed")

def test_division():
    assert division(5, 2) == 2.5
    print("Test division passed")


if __name__ == "__main__":
    test_addition()
    test_division()
