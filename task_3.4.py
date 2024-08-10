lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
if not lst:
    result = 0
else:
    even_index_sum = 0
for index,value in enumerate(lst):
    if index % 2 == 0:
        even_index_sum += value
        result = even_index_sum * lst[-1]
print(result)