from Prac6.guitar import Guitar
import datetime

current_year = datetime.date.today().year
# print(current_year)
# first_guitar = Guitar('name',year, cost=)
first_guitar = Guitar('Gibson L-5 CES', 1922, 16035.40)
print(first_guitar.year)
second_guitar = Guitar('Another Guitar', 2013, 198.35)
print(f'{first_guitar.name} get_age(), expected age is 100, got {first_guitar.get_age()}')
print(f'{second_guitar.name} get_age(), expected age is 9, got {second_guitar.get_age()}')
print(f'{first_guitar.name} is_vintage(), expected age is True, got {first_guitar.is_vintage()}')
print(f'{second_guitar.name} is_vintage(), expected age is False, got {second_guitar.is_vintage()}')


