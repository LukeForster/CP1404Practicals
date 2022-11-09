import csv
from Prac6.guitar import Guitar


def main():
    guitars = get_guitars()
    add_guitar(guitars)
    guitars.sort()
    for guitar in guitars:
        print(guitar)


def get_guitars():
    guitars = []
    with open('guitars.csv', 'r', newline='') as in_file:
        # in_file = open('guitars.csv', 'r', newline='')
        in_file.readline()
        # print(in_file.readline)
        reader = csv.reader(in_file)  # use default dialect, Excel
        for row in reader:
            # print(row)
            guitar = Guitar(row[0], row[1], float(row[2]))
            guitars.append(guitar)
            # print(guitar)
    in_file.close()
    return guitars


def add_guitar(guitars):
    menu_choice = input('Do you want to add a guitar? (Y/N): ').upper()
    while menu_choice == 'Y':
        try:
            name = input('Name: ')
            year = input('Year: ')
            cost = float(input('Cost: '))
            new_guitar = Guitar(name, year, cost)
            guitars.append(new_guitar)
            menu_choice = input('Do you want to add a guitar? (Y/N): ').upper()
        except ValueError:
            print('Invalid')
            menu_choice = input('Do you want to add a guitar? (Y/N): ').upper()
    return guitars

main()
