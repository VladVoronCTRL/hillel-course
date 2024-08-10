original_list = [0, 6, 0, 7, 12, 0, 22]

result = []
for num in original_list:
    if num != 0:
        result.append(num)
zero_count = original_list.count(0)
result.extend([0] * zero_count)
original_list[:] = result
print(original_list)