from Prac6.guitar import Guitar
import datetime

current_year = datetime.date.today().year

def add_guitar(name, year, cost, guitars):
    guitars.append(Guitar(name, year, cost))
    for i, guitar in enumerate(guitars, 1):
        print(guitar)



def main():
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