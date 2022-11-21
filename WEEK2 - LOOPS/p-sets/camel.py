Camel = input("Camel_case : ")
print("snake_case: ", end="")

for letter in Camel:
    if letter.isupper():
        print("_" + letter.lower(), end="")
    else:
        print(letter, end="")
print()
