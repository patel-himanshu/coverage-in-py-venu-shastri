import unittest
import credit_card_validator

class CreditCardValidator(unittest.TestCase):
	def test_credit_card_empty(self):
		self.assertFalse(credit_card_validator.validate(""))

	def test_credit_card_less_than_16(self):
		self.assertFalse(credit_card_validator.validate("123"))

	def test_credit_card_more_than_16(self):
		self.assertFalse(credit_card_validator.validate("123456789012345678"))

	def test_credit_card_valid_value(self):
		self.assertTrue(credit_card_validator.validate("4012888888881881"))

	def test_credit_card_invalid_value(self):
		self.assertFalse(credit_card_validator.validate("4012888888881889"))

if __name__ == "__main__":
	unittest.main()