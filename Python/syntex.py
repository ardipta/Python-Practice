print(1,2,3,4,5)
# Output: 1 2 3 4

print(1,2,3,4,sep='&')
# Output: 1&2&3&4&5

print(1,2,3,4,5,sep='#',end='\n')
# Output: 1#2#3#4&

x = 3; y = 5
print('The value of x is {} and y is {}'.format(x,y), end='\n')
#Output: The value of x is 3 and y is 5

print('I love {0} and {1}'.format('Me','Myself'))
# Output: I love Me and Myself

print('I love {1} and {0}'.format('Me','Myself'), end='\n')
# Output: I love Myself and Me

print('Hello {name}, {asking}'.format(asking = 'How are you?', name = 'Tamjid'))
#Output: Hello Tamjid How are you?
