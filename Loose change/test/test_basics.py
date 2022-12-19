from src.kata_loose_change import loose_change
import pytest

def test_basics_change():
    assert loose_change(29) ==  {'Nickels': 0, 'Pennies': 4, 'Dimes': 0, 'Quarters': 1}
def test_basics_change_all_pounds():
    assert loose_change(91) ==  {'Nickels': 1, 'Pennies': 1, 'Dimes': 1, 'Quarters': 3}
def test_basics_change_zero():
    assert loose_change(0) ==   {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
def test_basics_change_negative():
    assert loose_change(-2) ==  {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
def test_basics_change_float():
    assert loose_change(3.9) == {'Nickels': 0, 'Pennies': 3, 'Dimes': 0, 'Quarters': 0}