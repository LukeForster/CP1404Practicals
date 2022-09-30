print("Counting in 2's:")
for i in range(1, 21, 2):
    print(i, end=' ')
print()

print("Counting in 10's:")
for i in range(0, 100, 10):
    print(i, end=' ')
print()

print("Counting down from 20")
for i in range(20, 0, -1):
    print(i, end=' ')
print()

stars = int(input('How many stars would you like: '))
for i in range(0, stars, 1):
    print(end='*')

print('Stars as a triangle:')
for i in range(0, stars,1):
    for j in range(0, i+1, 1):
        print(end='*')
    print('')