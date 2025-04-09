mystring = "Nihal"
nihal = []
for i in mystring:
    nihal.append('100')
print(nihal)


nihal = [i for i in mystring]
print(nihal)


neha = [i for i in range(0,11) if i%2==0]
print(neha)


vaibhavi = [i if i%2==0 else 'ODD' for i in range(0,11)]
print(vaibhavi)


mylist = []
for i in [1,2,3]:
    for j in [1,10,100]:
        mylist.append(i*j)
print(mylist)


mylist1 = [i*j for i in [1,2,3] for j in [1,10,100]]
print(mylist1)