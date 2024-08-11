import random
lst_length = random.randint(3, 10)
random_lst = [random.randint(1, 100) for i in range(lst_length)]
print("Початковий список", random_lst)
new_list = [random_lst[0], random_lst[2], random_lst[-2]]
print("Новий список", new_list)
