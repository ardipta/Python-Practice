"""
23. Summing a Million: Make a list of the numbers from one to one million,
and then use min() and max() to make sure your list actually starts at one and
ends at one million. Also, use the sum() function to see how quickly Python can
add a million numbers.
"""
list_1 = list(range(1, 10001))
minimun = min(list_1)
maximum = max(list_1)
summation = sum(list_1)
print(minimun, maximum, summation)
