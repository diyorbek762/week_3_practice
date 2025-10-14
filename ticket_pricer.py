
age = int(input('Enter your age: '))
print('--- Movie Ticket Pricer ---')
print(f'Please enter your age: {age}')
if age <= 12:
    print("You fall into 'Children' category.")
    print('Your ticket price is: 8$')
elif age >= 65:
    print("You will fall into 'Senior' category.")
    print('Your ticket price is: 10$')
else:
    print("You fall into 'Adult' category.")
    print('Your ticket price is: 15$')