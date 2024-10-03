# Function to print n odd natural numbers
def print_n_odd_numbers(n):
    count = 0
    num = 1
    while count < n:
        print(num, end=' ')
        num += 2
        count += 1

# Take input from user
n = int(input("Enter the value of n: "))
print_n_odd_numbers(n)