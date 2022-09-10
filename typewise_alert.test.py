import unittest
import typewise_alert


class TypewiseTest(unittest.TestCase):
	def test_infers_breach_as_per_limits_too_low(self):
		self.assertTrue(typewise_alert.infer_breach(20, 50, 100) == 'TOO_LOW')

	def test_infers_breach_as_per_limits_too_high(self):
		self.assertTrue(typewise_alert.infer_breach(120, 50, 100) == 'TOO_HIGH')

	def test_infers_breach_as_per_limits_normal(self):
		self.assertTrue(typewise_alert.infer_breach(60, 50, 100) == 'NORMAL')

	def test_classify_temperaturee_breach_passive_cooling(self):
		self.assertTrue(typewise_alert.classify_temperature_breach('PASSIVE_COOLING', 10) == 'NORMAL')

	def test_classify_temperaturee_breach_hi_active_cooling(self):
		self.assertTrue(typewise_alert.classify_temperature_breach('HI_ACTIVE_COOLING', 50) == 'TOO_HIGH')

	def test_classify_temperaturee_breach_med_active_cooling(self):
		self.assertTrue(typewise_alert.classify_temperature_breach('MED_ACTIVE_COOLING', -10) == 'TOO_LOW')

	def test_function_calls(self):
		typewise_alert.send_to_controller("TOO_HIGH")
		typewise_alert.send_to_email("TOO_LOW")

if __name__ == '__main__':
	unittest.main()