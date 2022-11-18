from Prac9.unreliable_car import Unreliable


def main():
    """Test the taxi class"""
    bad_car = Unreliable('Craptiva', 100, 50)
    good_car = Unreliable('Hilux', 100, 99)
    for i in range(1, 12):
        print(f'{good_car.name} travelled {good_car.drive(i)}km')
        print(f'{bad_car.name} travelled {bad_car.drive(i)}km')
    print(good_car)
    print(bad_car)


main()
