number = int(input('enter a number: '))
a=0 
b=1
for l in range(number):
    print(a, end=" ")
    a, b = b, a+b
    

