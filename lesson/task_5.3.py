import string

text = input("Введіть рядок: ")

for char in string.punctuation:
    text = text.replace(char, "")

words = text.split()

for i in range(len(words)):
    words[i] = words[i][0].upper() + words[i][1:].lower()

hashtag = "#" + "".join(words)

if len(hashtag) > 140:
    hashtag = hashtag[:140]

if len(hashtag) == 1:
    hashtag = None

print(hashtag)
