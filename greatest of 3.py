# Function to find the greatest number among three numbers entered by the user using if-else statement
def find_greatest(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

# Get the numbers from the user and store them in variables `a`, `b`, and `c` respectively 
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))

# Call the function and store the result in a variable
greatest_number = find_greatest(a, b, c)
print(f"The greatest number is: {greatest_number}")