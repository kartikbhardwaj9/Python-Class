def count_digits(number):
    number_str = str(number)
    digit_count = len(number_str)
    return digit_count

number = int(input("Enter a number: "))
print(f"The number {number} has {count_digits(number)} digits.")