
def infer_breach(value, lowerLimit, upperLimit):
	if value < lowerLimit:
		return 'TOO_LOW'
	if value > upperLimit:
		return 'TOO_HIGH'
	return 'NORMAL'


def classify_temperature_breach(coolingType, temperatureInC):
	limits = {
		'PASSIVE_COOLING': [0, 35],
		'MED_ACTIVE_COOLING': [0, 40],
		'HI_ACTIVE_COOLING': [0, 45]
	}
	lowerLimit, upperLimit = limits[coolingType]
	return infer_breach(temperatureInC, lowerLimit, upperLimit)


def check_and_alert(alertTarget, batteryChar, temperatureInC):
	breachType =\
		classify_temperature_breach(batteryChar['coolingType'], temperatureInC)
	if alertTarget == 'TO_CONTROLLER':
		send_to_controller(breachType)
	elif alertTarget == 'TO_EMAIL':
		send_to_email(breachType)


def send_to_controller(breachType):
	header = 0xfeed
	print(f'{header}, {breachType}')


def send_to_email(breachType):
	recepient = "a.b@c.com"
	if breachType == 'TOO_LOW':
		print(f'To: {recepient}')
		print('Hello, the temperature is too low')
	elif breachType == 'TOO_HIGH':
		print(f'To: {recepient}')
		print('Hello, the temperature is too high')
