def validate(card_number):
	card_number_length = len(card_number) - 1

	if card_number == "":
		return False
	elif card_number_length != 15:
		return False

	numbers_list = [int(ch) for ch in card_number]
	check_digit = numbers_list.pop()
	result = 0
	
	for (index, number) in enumerate(numbers_list):
		if ((card_number_length - index) % 2 == 0):
			multiplier = 1
		else:
			multiplier = 2
		
		new_number = int(number) * multiplier
		if new_number > 9:
			new_number = (new_number % 10) + (new_number // 10)

		result += new_number
	
	computed_check_digit = 10 - (result % 10)
	return check_digit == computed_check_digit