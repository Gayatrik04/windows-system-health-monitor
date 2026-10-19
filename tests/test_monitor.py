import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from monitor import classify_usage


class TestClassifyUsage(unittest.TestCase):
    def test_normal_usage(self):
        self.assertEqual(classify_usage(45), "NORMAL")

    def test_threshold_is_high(self):
        self.assertEqual(classify_usage(80), "HIGH")

    def test_maximum_usage_is_high(self):
        self.assertEqual(classify_usage(100), "HIGH")

    def test_invalid_negative_value(self):
        with self.assertRaises(ValueError):
            classify_usage(-1)

    def test_invalid_over_100_value(self):
        with self.assertRaises(ValueError):
            classify_usage(101)


if __name__ == "__main__":
    unittest.main()
