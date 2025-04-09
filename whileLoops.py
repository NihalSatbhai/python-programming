x = 0
while x > 5:
    print(x)
    pass # pass will execute the rest of the code even if the loop fails
print("End of the Loop")

x = "string"
for i in x:
    if i == "t":
        break # it breaks the loop
    print(i)

x = "string"
for i in x:
    if i == "t":
        continue # it will go back to the start of the loop
    print(i)