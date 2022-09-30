import random
number_of_days = 1
OUTPUT_FILE = 'Prices.txt'
out_file = open(OUTPUT_FILE, 'w')

MAX_INCREASE = 0.175  # 17.5%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 1
MAX_PRICE = 100.00
INITIAL_PRICE = 10.0

price = INITIAL_PRICE
print("${:,.2f}".format(price))

while price >= MIN_PRICE and price <= MAX_PRICE:
    price_change = 0
    # generate a random integer of 1 or 2
    # if it's 1, the price increases, otherwise it decreases
    if random.randint(1, 2) == 1:
        # generate a random floating-point number
        # between 0 and MAX_INCREASE
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        # generate a random floating-point number
        # between negative MAX_DECREASE and 0
        price_change = random.uniform(-MAX_DECREASE, 0)

    price *= (1 + price_change)
    # print('On day', number_of_days, 'the price is: ${:,.2f}'.format(price), file=out_file)
    print(f'On day {number_of_days} the price is: {price:,.2f}', file=out_file)
    number_of_days = number_of_days + 1
out_file.close()




