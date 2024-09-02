import string
input_letters = input()
start, end = input_letters.split('-')
alphabet = string.ascii_letters
start_index = alphabet.index(start)
end_index = alphabet.index(end)
print(alphabet[start_index:end_index + 1])
