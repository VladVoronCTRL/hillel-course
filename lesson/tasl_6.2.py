total_seconds = int(input("Введіть кількість секунд: "))

days, remaining_seconds = divmod(total_seconds, 86400)
hours, remaining_seconds = divmod(remaining_seconds, 3600)
minutes, seconds = divmod(remaining_seconds, 60)

if days % 10 == 1 and days % 100 != 11:
    day_word = "день"
elif 2 <= days % 10 <= 4 and (days % 100 < 10 or days % 100 >= 20):
    day_word = "дні"
else:
    day_word = "днів"

hours = str(hours).zfill(2)
minutes = str(minutes).zfill(2)
seconds = str(seconds).zfill(2)

print(f"{days} {day_word}, {hours}:{minutes}:{seconds}")
