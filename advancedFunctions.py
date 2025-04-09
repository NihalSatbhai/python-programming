def myfunc(*args):
    return sum(args)
a = myfunc(1,2,3)
print(a)


def myfunc1(*args):
    list = []
    for i in args:
        if i%2 == 0:
            list.append(i)
        else:
            pass
    return list
a = myfunc1(1,2,3,4)
print(a)


def myfunc2(my_string):
    output_string = []
    for i in range(len(my_string)):
        if i % 2 == 0:
            output_string.append(my_string[i].lower())
        else:
            output_string.append(my_string[i].upper())
    return ''.join(output_string)
a = myfunc2('Anthropomorphism')
print(a)


def myfunc3(a,b):
    if a%2 == 0 and b%2 == 0:
        return min(a,b)
    elif a%2 == 0 or b%2 == 0:
        return max(a,b)
    else:
        return max(a,b)
a = myfunc3(2,4)
print(a)


def myfunc4(myString):
    if myString[0] == myString[myString.index(' ') + 1]:
        return True
    else:
        return False
a = myfunc4('Nihal Nalayak')
print(a)


def myfunc4(a,b):
    if a + b == 20:
        return True
    elif a == 20 or b == 20:
        return True
    else:
        return False
a = myfunc4(10,50)
print(a)