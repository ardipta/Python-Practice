dict_1 = {}
dict_2 = dict()

print(type(dict_1))
print(type(dict_2))

age_dict = {
    'key': 'value',
    'karim': 20,
    'Abul': 34,
    'Kashem': 12
}

print(age_dict)
print(age_dict.keys())
print(age_dict.values())
print(age_dict.items())
print(age_dict['Abul'])
print(age_dict.get('key'))
age_dict['python'] = 100  # insert values
del age_dict['Abul']  # delete values
print(age_dict)
