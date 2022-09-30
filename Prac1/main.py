name = input('What is your name: ')
print('What would you like to do: ')
print('H = Hello')
print('G = Goodbye')
print('Q = Quit')

choice = input('Enter Here: ').upper()
while choice != 'Q':

    if choice == 'H':
        print('Hello', name)
    elif choice == 'G':
        print('Goodbye', name)
    else:
        print('Invalid input, try again')
print('Quitting program')