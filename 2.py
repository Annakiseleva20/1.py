def selection_sort(numbers):
    for i in range(len(numbers)):
        min_idx = i
        for j in range(i+1, len(numbers)):
            if numbers[j] < numbers[min_idx]:
                min_idx = j
        numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]
    return numbers


numbers = [10, 8, 999, 6, 4, 1337, 2, 1]
sorted_numbers = selection_sort(numbers)
print(sorted_numbers)
