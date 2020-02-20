"""
19. Cities: Make a dictionary called cities. Use the names of three cities as
keys in your dictionary. Create a dictionary of information about each city and
include the country that the city is in, its approximate population, and one fact
about that city. The keys for each city’s dictionary should be something like
country, population, and fact. Print the name of each city and all of the information
you have stored about it.
"""
cities = {
    'dhaka': {
        'country': 'Bangladesh',
        'population': '1 crore',
        'fact': 'Digital Bangladesh'
    },
    'new york': {
        'country': 'USA',
        'population': '50 lakh',
        'fact': 'hollywood'
    },
    'delhi': {
        'country': 'India',
        'population': '2 crore',
        'fact': 'Bollywood'
    }
}

for i in cities.items():
    print(i)