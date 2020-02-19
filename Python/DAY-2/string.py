"""name1 = "python"

name2 = "Tutorial"
number1 = 17
number2 = 2.7
print(name1 + " " + name2 + " " + str(number1) + " " + str(number2))"""

"""print('{}, {}, {}'.format("a", "b", "c"))
print('{0}, {2}, {1}'.format("a", "b", "c"))"""

# formatting
name = "Python"
version = 3.5
# python 3.3 to 3.5
"""print("This is {python} programing language. Version is {version}".format(python=name, version=version))
print("This is {python} programing language. Version is {version}".format(python="Python", version=3.5))"""

# python 3.8
"""print(f'This is {name} programming language.\n'
      f'Version is {version}')"""

name = "Python language"
print(name.capitalize())
print(name.title())
print(name.upper())
print(name.lower())
print(name.swapcase())
print(len(name))
print(name.count("a"))
print(name.split("a"))
print(name.split(" "))
print(name.split())
# for more => print(name.__dir__()) use this command
