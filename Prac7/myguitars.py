import csv
from Prac6.guitar import Guitar


def main():
    guitars = get_guitars()
    add_guitar(guitars)
    guitars.sort()
    # for guitar in guitars:
    #     print(guitar)
    store_guitars(guitars)


def get_guitars():
    guitars = []
    with open('guitars.csv', 'r', newline='') as in_file:
        # in_file = open('guitars.csv', 'r', newline='')
        in_file.readlines()
        # print(in_file.readline)
        reader = csv.reader(in_file)  # use default dialect, Excel
        for row in reader:
            # print(row)
            guitar = Guitar(row[0], row[1], float(row[2]))
            # print(guitar)
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
            # print(new_guitar)
            guitars.append(new_guitar)
            menu_choice = input('Do you want to add a guitar? (Y/N): ').upper()
        except ValueError:
            print('Invalid')
            menu_choice = input('Do you want to add a guitar? (Y/N): ').upper()
    return guitars

def store_guitars(guitars):

    with open('guitars.csv', 'w', newline='') as out_file:  # Re-opens the movies.csv so that it can be updated
        writer = csv.writer(out_file)
        for guitar in guitars:
            save_guitar = []
            name = guitar.name
            save_guitar.append(name)
            # print(save_guitar)
            year = guitar.year
            save_guitar.append(year)
            # print(save_guitar)
            cost = guitar.cost
            save_guitar.append(cost)
            # print(save_guitar)
            writer.writerow(save_guitar)       # The csv writer will update the movies.csv with the updated list of movies



main()
