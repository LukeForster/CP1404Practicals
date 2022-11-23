from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def main():
    print('Less a Go')
    taxis = [Taxi('Prius', 100), SilverServiceTaxi('Limo', 100, 2), SilverServiceTaxi('Hummer', 200, 4)]
    total_cost = 0
    cost = 0
    menu(taxis, total_cost, cost)
    print(f'Final Cost: ${total_cost:.2f}')
    print('Taxis are now: ')
    for taxi in taxis:
        print(f'{taxi}')


def menu(taxis, total_cost, cost):
    print('q)uit, c)hoose taxi, d)rive ')
    menu_choice = input().lower()
    while menu_choice != 'q':
        if menu_choice == 'c':
            taxi_choice = choose_taxi(taxis)
        elif menu_choice == 'd':
            try:
                cost += drive_taxi(cost, taxi_choice, taxis)
            except UnboundLocalError:
                print('Select a taxi before driving')
        else:
            print('Invalid Selection')
        total_cost += cost
        print(f'Current total: ${cost:.2f}')
        print('q)uit, c)hoose taxi, d)rive ')
        menu_choice = input().lower()
    return total_cost


def choose_taxi(taxis):
    print('Taxis Available:')
    for taxi in taxis:
        print(f'{taxi}')
    taxi_choice = input('Choose Taxi: ').title()
    return taxi_choice


def drive_taxi(cost, taxi_choice, taxis):
    if taxi_choice == 'Prius':
        chosen_taxi = taxis[0]
        distance = int(input('How far would you like to travel: '))
        chosen_taxi.drive(distance)
        cost = chosen_taxi.get_fare()
        print(f'Your {chosen_taxi.name} trip is: ${cost:.2f}')
    elif taxi_choice == 'Limo':
        chosen_taxi = taxis[1]
        distance = int(input('How far would you like to travel: '))
        chosen_taxi.drive(distance)
        cost = chosen_taxi.get_fare()
        print(f'Your {chosen_taxi.name} trip is: ${cost:.2f}')
    elif taxi_choice == 'Hummer':
        chosen_taxi = taxis[2]
        distance = int(input('How far would you like to travel: '))
        chosen_taxi.drive(distance)
        cost = chosen_taxi.get_fare()
        print(f'Your {chosen_taxi.name} trip is: ${cost:.2f}')
    return cost


main()
