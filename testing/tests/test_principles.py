import sys
sys.path.append("../src")
#TODO make it with `pip install -e .`

from math_demo import (
    add,
    add_with_bug,
    calculate_tax_with_bug,
    calculate_tax
)

# Ранее тестирование позволяет съэкономить время позднее
# Тесты показывают наличие ошибок, а не отсутвие 
# Тесты не должны дублировать (и делать предположения о) логику(е) тестируемого кода
# Тесты не должны использовать ВСЕ наборы входных параметров
# Тесты должны покрывать "кластеры" входных параметров
# Тесты должны быть логически обособлены (single responsibility)
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

def test_addition_overcomplicated():
    # formally valid test but too slow
    for i in range(0, 2**32):
        for j in range(0, 2**32):
            assert add(i, j) == sum([i, j]) # might violate duplicate principle
            assert add(-i, j) == sum([-i, j])
            assert add(i, -j) == sum([i, -j])
            assert add(-i, -j) == sum([-i, -j])

def test_addition_reasonable():
    assert add(2, 2) == 4
    assert add(0, 0) == 0
    assert add(6, 7) == 13 
    assert add(-6, -7) == -13
    assert add(6, -7) == -1
    assert add(-7, 0) == -7
    assert add(7, 0) == 7
    print("Test ADDITION REASONBLE PASS")

def test_addition_commutative():
    # can be in previous test but logically separated
    assert add(7, -6) == 1
    assert add(-6, 7) == 1
    print("Test ADDITION is COMMUNITATIVE PASSED")

def test_tax_calucation_pesticised():
    # using only integers limits test case
    assert calculate_tax_with_bug(1000) == 150.0
    assert calculate_tax_with_bug(100) == 15.0
    assert calculate_tax_with_bug(10) == 1.5
    assert calculate_tax_with_bug(1) == 0.15
    assert calculate_tax_with_bug(245) == 36.75
    assert calculate_tax_with_bug(-200) == -30.
    assert calculate_tax_with_bug(0) == 0.
    print("Test TAX CALCULATION PASSED")
    # must fails with floats but I didn't used them
    #assert calculate_tax_with_bug(24.5) == 3.67 # 3.675

def test_tax_calucation():
    # using only integers limits test case
    assert calculate_tax_with_bug(1000) == 150.0
    assert calculate_tax_with_bug(100) == 15.0
    assert calculate_tax_with_bug(10) == 1.5
    assert calculate_tax_with_bug(1) == 0.15
    assert calculate_tax_with_bug(245) == 36.75
    assert calculate_tax_with_bug(-200) == -30.
    assert calculate_tax_with_bug(0) == 0.
    # using floats make additional test case not available with integers
    assert calculate_tax_with_bug(24.5) == 3.67 # 3.675
    print("Test TAX CALCULATION PASSED")



if __name__ == "__main__":
    test_addition()
    test_addition_with_bug()
    test_addition_duplicated()
    #test_addition_overcomplicated() # too redundant run on your own risk
    test_addition_reasonable()
    test_addition_commutative()
    test_tax_calucation_pesticised()
    test_tax_calucation()
