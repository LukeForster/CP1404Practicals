# Section 1 #

name = input('What is your name? ')
out_file = open('name.txt', 'w')
out_file.write(name)
out_file.close()

# Section 2 #

in_file = open('name.txt', 'r')
print('Your name is', in_file.read().strip())
in_file.close()

# Section 3 #


with open('numbers.txt', 'r') as in_file:
    number1 = int(in_file.readline())
    number2 = int(in_file.readline())
in_file.close()
print(number1+number2)

# Section 4 #

total = 0
with open('numbers.txt', 'r') as in_file:
    for line in in_file:
        number = int(line)
        total += number
in_file.close()
print(total)

