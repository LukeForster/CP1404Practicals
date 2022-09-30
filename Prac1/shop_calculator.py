number_of_items = int(input('How many items does the customer have: '))
total_cost = 0
while number_of_items < 1:
    print('Invalid input, try again')
    number_of_items = int(input('How many items does the customer have: '))

for i in range(1, number_of_items + 1, 1):
    print('Please enter item', i, 'cost:')
    item_cost = float(input())
    total_cost = float(total_cost + item_cost)
print('The customer total is: $', total_cost)
