def add_more_than_one_argument(numbers_list):
	if len(numbers_list) == 1:
		return int(numbers_list[0])
	elif len(numbers_list) == 2:
		a, b = int(numbers_list[0]), int(numbers_list[1])
		return a + b

def add(input_str):
    if input_str == "":
        return 0

    numbers_list = input_str.split(",")
    return add_more_than_one_argument(numbers_list)