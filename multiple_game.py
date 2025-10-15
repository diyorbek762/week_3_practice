#This is a classic programming interview question. 
# Write a program that prints the numbers from 1 to 100, each on a new line.
#  However, for multiples of three, print “Fizz” instead of the number. 
# For multiples of five, print “Buzz”. 
# For numbers which are multiples of both three and five, print “FizzBuzz”.
print('--- FizzBuzz Challenge (1-100) ---')
for i in range(1, 101):
    if i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    elif i % 15 == 0:
        print('FizzBuzz')
    else:
        print(i)


