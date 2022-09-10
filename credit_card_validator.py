def validate(card_number):
	if card_number == "":
		return False
	elif len(card_number) != 16:
		return False