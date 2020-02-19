set_1 = {1, 3, 5, 7, 9}

print(set_1)
print(type(set_1))

# Add single item
set_1.add(2)
set_1.add('hello')
print(set_1)

# Add multiple item
set_1.update([12, 44, 'Dipto'])
print(set_1)

# remove item
set_1.remove(44)
print(set_1)

# union operation
set_2 = {100, 300, 400, 'Dipto'}
print(set_1 | set_2)

# intersection
print(sorted(set_1 & set_2))

# to clear
set_1.clear()
print(set_1)
