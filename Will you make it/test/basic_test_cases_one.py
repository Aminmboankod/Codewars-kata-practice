from src.distance_fuel import zero_fuel
import pytest
@pytest.mark.case_true
def basic_test_cases():
    assert zero_fuel(50, 25, 2) == True