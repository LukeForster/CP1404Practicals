def get_password():
    i = 0
    while i != 1:
        password = input('Set password: ')
        min_length = 4
        if len(password) < min_length:
            print('Password needs to be longer')
        else:
            i = 1
    return password


def print_password():
    password = get_password()
    for i in range(0, len(password)):
        print(end='*')


print_password()