#! python3
"""
Ask the user to enter a number. 
Tell them if the number is a positive integer
(2 points) 

inputs:
a number of any type

outputs:
xx is a positive integer.
xx is not a positive integer

example:
Enter a number: -3
-3 is not a positive integer

Enter a number: 2.4
2.4 is not a positive integer

Enter a number: 5
5 is a positive integer

Enter a number: 4.0
4.0 is a positive integer
"""

x = float(input("\n\nEnter a number: "))
i = int(x)

if i == x and x > 0:
    print("Your number is a positive integer")
else:
    print("Your number is not a positive integer")
