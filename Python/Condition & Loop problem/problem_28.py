"""
28. Buffet: A buffet-style restaurant offers only five basic foods. Think of five
simple foods, and store them in a tuple.
• Use a for loop to print each food the restaurant offers.
• Try to modify one of the items, and make sure that Python rejects the
change.
• The restaurant changes its menu, replacing two of the items with different
foods. Add a block of code that rewrites the tuple, and then use a for
loop to print each of the items on the revised menu.
"""
tuple_1 = ('beef', 'chicken', 'rice', 'roast', 'mutton')
for i in tuple_1:
    print(i)

list_1 = list(tuple_1)
list_1[2] = 'plain rice'
list_1[1] = 'biriyani'
tuple_1 = tuple(list_1)
print("\nAfter Revised:")
for i in tuple_1:
    print(i)