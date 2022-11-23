from taxi import Taxi
from silver_service_taxi import  SilverServiceTaxi

def main():
    print('Less a Go')
    print('q)uit, c)hoose taxi, d)rive ')
    menu_choice = input().lower
    while menu_choice != 'q':
        if menu_choice == 'c':
            print('things')
        elif menu_choice == 'd':
            print('things2')
        else:
            print('Invalid Selection')

main()