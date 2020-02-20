"""
18. Pets: Make several dictionaries, where the name of each dictionary is the
name of a pet. In each dictionary, include the kind of animal and the owner’s
name. Store these dictionaries in a list called pets. Next, loop through your list
and as you do print everything you know about each pet.
"""
dog_dict = {
    'slam dog': 'john',
    'big dog': 'roman reign'
}
cat_dict = {
    'persian cat': 'lona',
    'Russian blue': 'steven'
}
bird_dict = {
    'parrot': 'kabir',
    'finch': 'eva'
}
pets = []
pets.append(dog_dict)
pets.append(cat_dict)
pets.append(bird_dict)
for pet in pets:
    print(pet)

