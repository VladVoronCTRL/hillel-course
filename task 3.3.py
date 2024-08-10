original_list = [1, 2, 3, 4, 5]
length = len(original_list)
result = [[], []]
if length == 0:
    result = [[], []]
else:
    middle_index = (length + 1) // 2
    first_half = original_list[:middle_index]
    second_half = original_list[middle_index:]
    result = [first_half, second_half]
print(result)