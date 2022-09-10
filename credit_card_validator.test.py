import unittest
import credit_card_validator

class CreditCardValidator(unittest.TestCase):
	def test_credit_card_empty(self):
		self.assertFalse(credit_card_validator.validate(""))

	def test_credit_card_less_than_16(self):
		self.assertFalse(credit_card_validator.validate("123"))

	def test_credit_card_more_than_16(self):
		self.assertFalse(credit_card_validator.validate("123456789012345678"))

if __name__ == "__main__":
	unittest.main()