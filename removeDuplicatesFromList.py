# Taking user input
duplicate_list = (input('Enter your list separated by commas: '))

# Convert input string into list and strip it
input_list = duplicate_list.split(',')
input_list = [item.strip() for item in input_list]

sorted_list = []

for i in input_list:
  if i not in sorted_list:
    sorted_list.append(i)

print(sorted_list)