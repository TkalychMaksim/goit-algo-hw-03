import random

def get_numbers_ticket(min_num, max_num, quantity):
    # Checking incoming params
    if min_num < 1 or max_num > 1000 or quantity < 1 or quantity > (max_num - min_num + 1):
        print("Incorrect function params")
        return []

    # Generating set of random numbers
    unique_numbers = set()
    while len(unique_numbers) < quantity:
        number = random.randint(min_num, max_num)
        unique_numbers.add(number)

    # Sorting set of numbers
    return sorted(unique_numbers)


