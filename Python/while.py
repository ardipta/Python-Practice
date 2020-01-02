n = int(input("Enter n: "))

count = 1
sum = 0


while count <= n:
    sum = sum + count
    count = count + 1    # update counter
print("The sum is", sum)


counter = 0

while counter < n:
    print("Inside while loop")
    counter = counter + 1
else:
    print("Inside  else ")
