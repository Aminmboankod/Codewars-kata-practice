from src.distance_fuel import zero_fuel
import pytest
@pytest.mark.case_false

def basic_test_cases():
    assert zero_fuel(100, 50, 1) == False