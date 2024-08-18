while True:
    number = input("введіть перше число: ")
    number = int(number)
    action = input("введіть дію")
    number_2 = input("введіть друге чилсо")
    number_2 = int(number_2)

    if action == "+":
        print(number + number_2)
    elif action == "-":
        print(number - number_2)
    elif action == "*":
        print(number * number_2)
    elif action == "/":
        if number_2 == 0:
            print("на нуль ділити не можна ")

        else:
            action = int(number / number_2)
            print(action)

    continue_calc = input("продовжити обчислення ? (y/n):")
    if continue_calc != "y":
        print("до побачення")
        break
