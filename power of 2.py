def power_2(number):
    if number == 0:    
      return 0
    if ((number & (~(number - 1))) == 0):
       return 1
    return 0

number = int(input("Enter the number : "))

if power_2(number):
   print("\n The number is your power of 2")
else:
   print("\nThe number is power of 2")
