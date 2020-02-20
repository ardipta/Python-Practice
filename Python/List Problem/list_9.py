"""
9.	Write a Python program to find the second smallest number in a list.
"""
list_1 = [3, 5, 1, 7, 15, 9]
min1 = min(list_1)
list_1.remove(min1)
min2 = min(list_1)
print("Second largest:", min2)
