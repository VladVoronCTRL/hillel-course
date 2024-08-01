number = (input("Enter a number: "))
number = int(number)
print(number // 1000)
hundredths = (number // 100) %10
print(hundredths)
tenths = (number // 10) %10
print(tenths)
units = (number // 1) %10
print(units)


