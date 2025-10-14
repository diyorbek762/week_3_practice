total = 0
number = input("Enter a number or done: ")
print("--- Running Total Calculator ---")
print("Enter numbers to add them up. Type 'done' to see the total.")
while number != "done":
     total += float(number)
     print(total)
     number = input("Enter a number or 'done': ")
     
     if number == "done":
          print(total)
          break