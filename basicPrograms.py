# check for the even number in list
my_iterable = [1,2,3,4,5,6]
for num in my_iterable:
    if num % 2 == 0:
        print (f'Even Number: {num}') # Formatting with String
    else:
        print ('Odd Number:' + str(num)) # String Concatenation

# Sum of all elements in list
sum = 0
for num in my_iterable:
    sum = sum + num
print (f'Sum of all elements in list: {sum}')

# Tuple Unpacking
tup = [(1,2), (3,4), (5,6)]
for a in tup:
    print (a)
for a,b in tup:
    print (a)
    print (b)

# Iterating Through Dictionaries (Note: Dictionaries Works Like Tuple Unpacking)
dict = {'k1':1, 'k2':2, 'k3':3}
for key,value in dict.items():
    print (key)
    print (value)

