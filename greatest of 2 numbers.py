#Function to find the greatest number between two numbers entered by the user using if - else statement
def find_greatest(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return "Both numbers are equal"

# Get the numbers from the user and store them in variables `a` and `b` respectively 
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

# Call the function and store the result in a variable  stored in th defined function
greatest_number = find_greatest(a, b)
print(f"The greatest number is: {greatest_number}")