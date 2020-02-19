# declaration

list_1 = []
list_2 = ["python", "python", 1, 3.6, True, False]
list_3 = list(("python", "python", 1, 3.6, True, False))

list_1.append(5)  # when insert single data at any position
print(list_1)
list_1.extend([list_2])  # when insert full list use extend
print(list_1)
list_1.extend(list_2)
print(list_1)
list_1.insert(0, 5)
list_1.insert(0, list_2)
print(list_1)

print(list_3)
print(list_2)

fruits = ['Apple', 'Orange', "Banana", "Mango"]

print(fruits)
print(fruits[2])
print(len(fruits))
fruits.remove('Orange')
print(fruits[:])
fruits.reverse()
print(fruits[:])
fruits.sort()  # ascending order
print(fruits[:])
fruits.sort(reverse=True)  # descending order
print(fruits[:])

print(fruits[:])
print(fruits[0:])
print(fruits[2:])
print(fruits[:2])
print(fruits[:-1])
print(fruits[:: 2])
print(fruits[:: -2])
