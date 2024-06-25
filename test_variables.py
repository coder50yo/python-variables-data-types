# test_variables.py
import unittest
from variables import *

class TestVariables(unittest.TestCase):
    def test_integer(self):
        self.assertIsInstance(integer_number, int)
        self.assertEqual(integer_number, 10)

    def test_float(self):
        self.assertIsInstance(float_number, float)
        self.assertAlmostEqual(float_number, 10.5)

    def test_string(self):
        self.assertIsInstance(string_text, str)
        self.assertEqual(string_text, "Hello, Python!")

    def test_boolean(self):
        self.assertIsInstance(boolean_value, bool)
        self.assertTrue(boolean_value)

    def test_list(self):
        self.assertIsInstance(list_example, list)
        self.assertEqual(list_example, [1, 2, 3, 4, 5])

    def test_tuple(self):
        self.assertIsInstance(tuple_example, tuple)
        self.assertEqual(tuple_example, (1, 2, 3, 4, 5))

    def test_dictionary(self):
        self.assertIsInstance(dictionary_example, dict)
        self.assertEqual(dictionary_example, {"name": "Alice", "age": 30})

    def test_set(self):
        self.assertIsInstance(set_example, set)
        self.assertEqual(set_example, {1, 2, 3, 4, 5})

    def test_none(self):
        self.assertIsNone(none_value)

if __name__ == "__main__":
    unittest.main()
