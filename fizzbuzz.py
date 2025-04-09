mylist = ['nihal', 'vaibhavi', 'sarthak', 'sakshi']
for i in mylist:
    i.split()
    if i[0] == 's':
        print(i)

for i in range(0,11):
    if i%2 == 0:
        print(i)

list1 = [i for i in range(1,50) if i%3 ==0]
print(list1)

st = 'Print every word in this sequence that has an even number of letters'
st1 = st.split()
for i in st1:
    if len(i) % 2 == 0:
        print(i)

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)