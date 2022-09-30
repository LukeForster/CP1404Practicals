"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    Ans - When the user input is not a number
2. When will a ZeroDivisionError occur?
    Ans - When the user input for the denominator is zero
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    Ans -  Perhaps
"""
numerator = int(input("Enter the numerator: "))
denominator = int(input("Enter the denominator: "))

try:
    while denominator == 0:
        denominator = int(input("Invalid denominator, please re-enter: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")