def my_function():
    return "python"


print(my_function())


def my_function_1(num_1, num_2):  # parameter
    return num_1 + num_2


print("sum_1 :", my_function_1(10, 12))  # positional argument
print("sum_1 :", my_function_1(num_1=10, num_2=15))  # keyword argument


def my_function_2(name, number):  # parameter
    return name + str(number)


print("sum_1 :", my_function_2('Python ', 12))  # positional argument
print("sum_1 :", my_function_2(name='python ', number=15))  # keyword argument


def my_function_3(num1, num2=100):
    return num1 + num2


print("sum_1 : ", my_function_3(10))


def calculate(*num):
    sum_1 = 0
    for i in num:
        sum_1 += i
    return sum_1


print(calculate(12, 34, 56, 75, 864))


def keyword_argument(**kwargs):  # kwargs = dictionary
    return kwargs


print(keyword_argument(age=12, name='python', id='123'))

my_dict = {
    'age': 12,
    'name': 'python',
    'id': 123,
}
print(keyword_argument(**my_dict))


def sum_sub(num1, num2):
    sum = num1 + num2
    sub = num1 - num2
    return sum, sub


a, b = sum_sub(100, 50)
print(a, b)

