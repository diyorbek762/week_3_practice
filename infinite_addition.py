#Using a while loop to repeat an action an unknown number of times.
#Initializing an “accumulator” variable (like total) to zero before the loop.
#Using an if statement inside the loop to check for the stop condition (“done”).
#Using break to exit the loop.
#Converting input to a number with float() to allow for decimals.
print('           --- Running Total Calculator ---')
print("Enter numbers to add them up. Type 'done' to see the total.")
number = (input("Enter a number or 'done': "))
zero = 0
while number != 'done':
    print(float(number))
    zero += float(number)
    print()
    print(f"Current Total: {zero}")
    if number == 'done':
       print(f'Total amount: {zero}')
    else:
        continue


