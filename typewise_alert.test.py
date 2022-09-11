import unittest
import typewise_alert
from unittest.mock import patch, call


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

	@patch('builtins.print')
	def test_send_to_controller(self, mock_print):
		typewise_alert.send_to_controller('TOO_LOW')
		mock_print.assert_called_with(f'{0xfeed}, TOO_LOW')

	@patch('builtins.print')
	def test_send_to_email_too_low(self, mock_print):
		typewise_alert.send_to_email('TOO_LOW')
		assert mock_print.mock_calls == [call('To: a.b@c.com'), call('Hello, the temperature is too low')]

	@patch('builtins.print')
	def test_send_to_email_too_high(self, mock_print):
		typewise_alert.send_to_email('TOO_HIGH')
		assert mock_print.mock_calls == [call('To: a.b@c.com'), call('Hello, the temperature is too high')]

	@patch('typewise_alert.send_to_controller')
	def test_check_and_alert_controller(self, mock):
		batteryChar = { 'coolingType': 'MED_ACTIVE_COOLING' }
		typewise_alert.check_and_alert('TO_CONTROLLER', batteryChar, 100)
		self.assertTrue(mock.called)

	@patch('typewise_alert.send_to_email')
	def test_check_and_alert_email(self, mock):
		batteryChar = { 'coolingType': 'HI_ACTIVE_COOLING'}
		typewise_alert.check_and_alert('TO_EMAIL', batteryChar, 30)
		self.assertTrue(mock.called)


if __name__ == '__main__':
	unittest.main()