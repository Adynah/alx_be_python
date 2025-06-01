# Define the number of rows for the pyramid
rows = 5

# Outer loop to control the number of rows
i = 1
while i <= rows:
    # Print spaces
    space = 1
    while space <= rows - i:
        print(" ", end="")
        space += 1

    # Print asterisks
    star = 1
    while star <= (2 * i - 1):
        print("*", end="")
        star += 1

    # Move to the next line
    print()
    i += 1
