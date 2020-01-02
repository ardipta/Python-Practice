print(range(10))
# Output: range(0, 10)
 
print(list(range(10)))
# Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
 
print(list(range(3,6)))
# Output: [3, 4, 5]

print(list(range(3, 20, 4)))
# Output: [3, 7, 11, 15, 19]

color = ['red','green','blue']

for i in range(len(color)):
	print("I like",color[i])
# Output:
# My favourite color is red
# My favourite color is green
# My favourite color is blue
    
                            
list_of_digits = [0,1,2,3,4,5,6,7,8,9]

input_digit = int(input('Enter a digit: '))

for i in list_of_digits:
	if input_digit == i:
		print("Digit is in the list")
		break
	else:
		print("Digit not found in list")

