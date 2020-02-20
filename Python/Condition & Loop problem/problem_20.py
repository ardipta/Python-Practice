"""
20. Multiples of Ten: Ask the user for a number, and then report whether the
number is a multiple of 10 or not.
"""
number = int(input())

if number % 10 == 0:
    print(str(number) + " is multiple of ten.")
else:
    print(str(number) + " is not multiple of ten.")
