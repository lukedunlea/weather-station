"""Basic test suite."""

import utils
from config import Config
from thresholds import ThresholdChecker

def test_utils():
    assert utils.celsius_to_fahrenheit(0) == 32
    print("✓ Utils test passed")

def test_thresholds():
    checker = ThresholdChecker(15, 30, 30, 70)
    alerts = checker.check_all(22, 50)
    assert len(alerts) == 0
    print("✓ Thresholds test passed")

if __name__ == "__main__":
    test_utils()
    test_thresholds()
    print("\n✓ All tests passed!")
