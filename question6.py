def analyze_numbers(numbers):
    total_sum = sum(numbers)
    average = total_sum / len(numbers)
    highest = max(numbers)
    lowest = min(numbers)
    even_count = sum(1 for num in numbers if num % 2 == 0)
    odd_count = sum(1 for num in numbers if num % 2 != 0)

    return total_sum, average, highest, lowest, even_count, odd_count


def numbers_above_average(numbers, average):
    return [num for num in numbers if num > average]


# Input Section: Convert space-separated string inputs into an integer list
input_string = input("Enter space-separated integers: ")
numbers = [int(x) for x in input_string.split()]

# Call first function and unpack returned analysis
total, avg, high, low, even_cnt, odd_cnt = analyze_numbers(numbers)

# Call second function to get list of numbers greater than average
above_avg_list = numbers_above_average(numbers, avg)

# Display Section
print("\n--- Number Analysis Results ---")
print(f"Sum of Numbers: {total}")
print(f"Average: {avg:.2f}")
print(f"Highest Number: {high}")
print(f"Lowest Number: {low}")
print(f"Even Number Count: {even_cnt}")
print(f"Odd Number Count: {odd_cnt}")
print(f"Numbers Above Average ({avg:.2f}): {above_avg_list}")