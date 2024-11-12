def count_in_set(input_set):
    all_digits = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}

    digit_counts = {digit: 0 for digit in all_digits}

    for digit in input_set:
        if digit in digit_counts:
            digit_counts[digit] += 1

    max_count = max(digit_counts.values())
    most_frequent = [digit for digit, count in digit_counts.items() if count == max_count]

    return most_frequent, max_count


input_set = '2244412'
most_frequent, max_count = count_in_set(input_set)

print(f"Цифри, яких найбільше: {most_frequent}")
print(f"Кількість їх появ: {max_count}")