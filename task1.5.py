def check_even(num):
    return num % 2 == 0

list_of_numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(check_even, list_of_numbers))
print(even_numbers)