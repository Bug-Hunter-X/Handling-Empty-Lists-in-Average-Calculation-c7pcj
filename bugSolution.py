def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    total = sum(numbers)
    average = total / len(numbers)
    return average

my_numbers = [1, 2, 3, 4, 5]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list)
print(f"The average of an empty list is: {average_empty}")

# Additional test cases to enhance robustness:
my_negative_numbers = [-1,-2,-3]
average_negative = calculate_average(my_negative_numbers)
print(f"The average of negative numbers is: {average_negative}")

my_mixed_numbers = [1,-2,3,-4,5]
average_mixed = calculate_average(my_mixed_numbers)
print(f"The average of mixed numbers is: {average_mixed}") 