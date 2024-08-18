import keyword
import string

variable_name = input("Введіть ім'я змінної: ")

is_valid = True

if variable_name[0].isdigit():
    is_valid = False

if any(char.isupper() for char in variable_name):
    is_valid = False

for char in variable_name:
    if char in string.punctuation.replace("_", "") or char.isspace():
        is_valid = False
        break

if variable_name in keyword.kwlist:
    is_valid = False

if variable_name.count("_") > 1:
    is_valid = False

print(is_valid)
