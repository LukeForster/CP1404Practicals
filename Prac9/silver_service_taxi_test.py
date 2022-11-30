from Prac9.silver_service_taxi import SilverServiceTaxi


def main():
    '''Test the silver service taxi class'''
    my_taxi = SilverServiceTaxi('Prius 1', 100, 2)
    my_taxi.drive(18)
    print(my_taxi)
    print(my_taxi.get_fare())


main()