import random

numbers_per_line = 6

number_of_lines = int(input('How many picks? '))
while number_of_lines < 0:
    print("That makes no sense!")
    print('Must be an integer')
    number_of_quick_picks = int(input("How many quick picks? "))


for line_number in range(number_of_lines):
    quick_picks = []
    for numbers in range(numbers_per_line):
        number = random.randint(1, 45)
        while number in quick_picks:
            number = random.randint(1, 45)
        quick_picks.append(number)
    # print(sorted(quick_picks))
    print(' '.join(f'{number:2}' for number in quick_picks))