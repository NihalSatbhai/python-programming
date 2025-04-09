def macd(myString):
    first_letter = myString[0]
    middle_part = myString[1:3]
    fourth_letter = myString[3]
    rest = myString [4: ]
    return first_letter.upper() + middle_part + fourth_letter.upper() + rest
result = macd('macdonalds')
print(result)


def reverse_string(myString):
    splitString = myString.split()
    reverseList = splitString[::-1]
    return ' '.join(reverseList)

result = reverse_string('I am Nihal')
print(result)