import sys
sys.path.append("../src")
#TODO make it with `pip install -e .`

from math_demo import (
    add,
    add_with_bug
)

# Ранее тестирование позволяет съэкономить время позднее
# Тесты показывают наличие ошибок, а не отсутвие 
# Тесты не должны дублировать (и делать предположения о) логику(е) тестируемого кода
# Тесты не должны использовать ВСЕ наборы входных параметров
# Тесты должны покрывать "кластеры" входных параметров
# Тесты должны обнаруживать новые ошибки (pescicide paradox)
# Тесты покрывают как успешные так и ошибочные кейсы

def test_addition():
    assert add(2, 2) == 4, "Function did not return 4"
    print("Test BASIC ADDITION PASSED")

def test_addition_with_bug():
    assert add_with_bug(2, 2) == 4, "Function did not return 4"
    assert add_with_bug(0, 0) == 0
    print("Test BUGGED ADDITION PASSED (does it mean code ok?)")
    #assert add_with_bug(6, 7) == 13 # will fail here

def test_addition_duplicated():
    # is it real good test (relies on absence of + in add())
    assert add(2, 3) == 2 + 3
    

if __name__ == "__main__":
    test_addition()
    test_addition_with_bug()
    test_addition_duplicated()
