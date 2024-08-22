num = int(input("Enter a number: "))

while num > 9:
    res = 1
    for digit in str(num):
        res *= int(digit)
        num = res
print(f'result is {num}')
