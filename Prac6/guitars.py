from Prac6.guitar import Guitar
import datetime

current_year = datetime.date.today().year


def add_guitar(name, year, cost, guitars):
    """Adds a guitar to the list, then checks if it is vintage and prints its details"""
    guitars.append(Guitar(name, year, cost))
    for i, guitar in enumerate(guitars, 1):
        print(guitar)



def main():
    """Initialises the program, used as menu mainly"""
    guitars = []
    new_guitar = input('Do you want to add a guitar? (Y/N): ').upper()
    while new_guitar == 'Y':
        try:
            name = str(input('Name: '))
            year = int(input('Year: '))
            cost = float(input('Cost: '))
            add_guitar(name, year, cost, guitars)
            new_guitar = input('Do you want to add a guitar? (Y/N): ').upper()
        except ValueError:
            print('Invalid')
            new_guitar = input('Do you want to add a guitar? (Y/N): ').upper()


if __name__ == '__main__':
    main()
