index_count = 0
for i in "Nihal":
    print("At index {} the letter is {}".format(index_count,i))
    index_count += 1


word = "word"
for i,j in enumerate(word):
    print(i)
    print(j)
    print('\n')


mylist = [1,2,3]
mylist1 = ['a', 'b', 'c']
for i,j in zip(mylist,mylist1):
    print(i)
print(min(mylist))
print(max(mylist1))


random = input("Enter your name: ")
print(f'your name is {random}')