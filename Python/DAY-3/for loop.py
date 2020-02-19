for i in range(10):
    print(i, end='\n')

for i in range(1, 10, 2):  # 2 increment range 1 to 10
    print(i, end='\n')

list_1 = ["python", "programming", "Language"]
for i in list_1:
    print(i, end='\n')

age_dict = {
    'key': 'value',
    'karim': 20,
    'Abul': 34,
    'Kashem': 12
}

for i in age_dict.items():
    print(i, end='\n')

for key, value in age_dict.items():
    print(key, ":", value)

for key in age_dict.keys():
    print(key)

for value in age_dict.values():
    print(value)

for i in range(10):
    for j in range(i):
        print("*", end = " ")
    print()