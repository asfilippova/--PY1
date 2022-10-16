list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max_num = list_numbers[0]
for num in list_numbers:
    if max_num < num:
        max_num = num

list_numbers[list_numbers.index(max_num)], list_numbers[-1] = list_numbers[-1], list_numbers[list_numbers.index(max_num)]

print(list_numbers)
