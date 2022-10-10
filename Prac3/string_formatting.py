## Using f-string

name = "Gibson L-5 CES"
year = 1922
cost = 16035.4
# print(cost)
print(f"My {name} was first made in {year} (that's right, {year}!)")
print(f'{year} {name} for about ${cost:,.0f}')

print(' ')

## Using for loop

for i in range(0, 200, 50):
    print(f'{i:4}')



