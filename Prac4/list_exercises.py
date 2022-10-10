numbers = []
print('Please Enter 5 Numbers')
while len(numbers) <= 4:
    try:
        new_number = int(input())
        numbers.append(new_number)
    except ValueError:
        print('Input must be an integer')
print(numbers)
print('The first number is:  {}'.format(*numbers))
print('The second number is: {1}'.format(*numbers))
print('The third number is:  {2}'.format(*numbers))
print('The fourth number is: {3}'.format(*numbers))
print('The fifth number is:  {4}'.format(*numbers))

#### Part 2 ####

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username_check = input('Please Enter Your Username: ')
print(len(usernames))
if username_check in usernames:
    print('Access Granted')
else:
    print('Access Denied')
