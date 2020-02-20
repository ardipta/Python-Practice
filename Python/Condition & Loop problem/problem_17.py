"""
17. Polling:
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
• Make a list of people who should take the favorite languages poll. Include
some names that are already in the dictionary and some that are not.
• Loop through the list of people who should take the poll. If they have
already taken the poll, print a message thanking them for responding.
If they have not yet taken the poll, print a message inviting them to take
the poll.
"""

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
people_list = ['sarah', 'dipto', 'ashik', 'jen', 'edward', 'john']

for poll in people_list:
    if poll in favorite_languages:
        print(poll + ", Thanks for responding.")
    else:
        print(poll + " You are invited to take the poll")