import unittest
import string_calculator


class StringCalculatorTest(unittest.TestCase):
  def test_given_empty_string_as_argument(self):
    self.assertTrue(string_calculator.add("") == 0)

#   def test_given_single_value_in_string_as_argument(self):
#     self.assertTrue(string_calculator.add("2") == 2)

#   def test_given_two_values_in_string_as_argument(self):
#     self.assertTrue(string_calculator.add("2,3") == 5)

if __name__ == '__main__':
  unittest.main()
