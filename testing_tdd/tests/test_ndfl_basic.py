#import sys
#sys.path.append("../src")

from ndfl import calculate_ndfl_tax

#| **До 2,4 млн руб.** | 13% | 13% от дохода |
#| **2,4 – 5 млн руб.** | 15% | 312 000 + 15% с суммы превышения |
#| **5 – 20 млн руб.** | 18% | 702 000 + 18% с суммы превышения |
#| **20 – 50 млн руб.** | 20% | 3 402 000 + 20% с суммы превышения |
#| **Свыше 50 млн руб.** | 22% | 9 402 000 + 22% с суммы превышения |

def test_ndfl_tier_1():
    assert calculate_ndfl_tax(500_000) == 65_000

def test_ndfl_tier_2():
    assert calculate_ndfl_tax(4_000_000) == 552_000

def test_ndfl_tier_3():
    assert calculate_ndfl_tax(10_000_000) == 1_602_000

#TODO make last two tiers