def print_pattern(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end="")
        print()

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print_pattern(num)