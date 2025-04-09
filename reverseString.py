def reverse_string():
    # Take user input as a string
    user_input = input("Enter a string to reverse: ")
    
    # Initialize an empty string for the reversed version
    reversed_string = ""
    
    # Loop through the input string in reverse order
    for i in range(len(user_input) -1, -1, -1):
        reversed_string += user_input[i]
    
    # Return the reversed string
    return reversed_string

# Call the function and print the result
result = reverse_string()
print("Reversed string:", result)