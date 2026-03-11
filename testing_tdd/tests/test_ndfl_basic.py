#import sys
#sys.path.append("../src")

from ndfl import calculate_ndfl_tax

def test_ndfl():
    assert calculate_ndfl_tax() == None