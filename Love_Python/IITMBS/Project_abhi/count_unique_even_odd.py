def count_unique_even_odd(l: list) -> dict:
    # Use sets to get unique numbers
    unique_numbers = set(l)

    # Initialize counters
    count_even = 0
    count_odd = 0

    # Iterate over unique numbers
    for num in unique_numbers:
        if num % 2 == 0:
            count_even += 1
        else:
            count_odd += 1

    return {'even': count_even, 'odd': count_odd}

l = [1, 1, 1]  # Corrected list
print(count_unique_even_odd(l))
