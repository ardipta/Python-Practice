"""
16. Rivers: Make a dictionary containing three major rivers and the country
each river runs through. One key-value pair might be 'nile': 'egypt'.
• Use a loop to print a sentence about each river, such as The Nile runs
through Egypt.
• Use a loop to print the name of each river included in the dictionary.
• Use a loop to print the name of each country included in the dictionary.
"""
river_dict = {
    'nile': 'egypt',
    'Volga': 'russia',
    'Ganges': 'india',
}
for river in river_dict:
    if river == 'nile':
        print(river + " runs through Egypt")
    elif river == 'Volga':
        print(river + " runs through Russia")
    elif river == 'Ganges':
        print(river + " runs through India")
