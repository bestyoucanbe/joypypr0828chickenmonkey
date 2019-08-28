# Instructions
# Write a program that prints the numbers from 1 to 100. You can use Python's range() to quickly make a list of numbers.

# For multiples of five (5, 10, 15, etc.) print "Chicken" instead of the number
# For the multiples of seven (7, 14, 21, etc.) print "Monkey".
# For numbers which are multiples of both five and seven print "ChickenMonkey".
# To determine if a number can be evenly divided by 5 or 7, use the Python modulo operator.


for i in range(1, 101, 1):
    if (i % 5) is 0 and (i % 7) is 0:
        print(f'{i} is divisible by both--so, chickenmonkey')
    elif (i % 5) is 0:
        print(f'{i} is divisible by 5--so, chicken')
    elif (i % 7) is 0:
        print(f'{i} is divisible by 7--so, monkey')
    else:
        # otherwise print the number
        print(f'i = {i}')
