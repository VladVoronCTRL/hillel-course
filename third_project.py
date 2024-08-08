number = (input("введіть 5-значне число: "))
number = int(number)
number_one = (number // 10000)
hundredths = (number // 1000) % 10
tenths = (number // 100) % 10
units = (number // 10) % 10
number_five = (number % 10)
reversed_number= (number_five * 10000  + units  * 1000 + tenths * 100 + hundredths * 10 + number_one)
print("перевернуте число:", reversed_number)
