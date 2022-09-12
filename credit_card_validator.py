def find_multiplier(card_number_length, index):
	if ((card_number_length - index) % 2 == 0):
		return 1
	else:
		return 2

def find_new_number(number, multiplier):
	new_number = int(number) * multiplier
	if new_number > 9:
		return (new_number % 10) + (new_number // 10)
	return new_number

def compute_check_digit(numbers_list, card_number_length):
	result = 0
	for (index, number) in enumerate(numbers_list):
		multiplier = find_multiplier(card_number_length, index)	
		new_number = find_new_number(number, multiplier)
		result += new_number
	return 10 - (result % 10)
	
def validate(card_number):
	card_number_length = len(card_number) - 1

	if card_number == "":
		return False
	elif card_number_length != 15:
		return False

	numbers_list = [int(ch) for ch in card_number]
	check_digit = numbers_list.pop()
	
	computed_check_digit = compute_check_digit(numbers_list, card_number_length)
	return check_digit == computed_check_digit