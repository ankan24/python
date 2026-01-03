# String - A sequence of characters used to store and manipulate text data.
str1 = "Ankan"
str2 = 'Apna\nCollege'
str3 = """This is a multi-line
string example."""

# /n is used for new line
# /t is used for tab space
# \ is used to escape characters

print(str1+" "+str2) # Concatenation of strings
print(len(str1)) # Length of the string
print(str2.upper()) # Convert to uppercase
print(str2.lower()) # Convert to lowercase
print(str3.split()) # Split the string into a list of words
print(str2.replace("Apna", "My")) # Replace substring
print(str1[0]) # Accessing first character
print(str1[1:4]) # Slicing the string from index 1 to 3
print(str1[-5:-3]) # Slicing using negative indices 
print(str1.index("k")) # Finding index of a character

str = " hello World! "
print(str.endswith("!")) # Check if string ends with a specific character
print(str.startswith(" H")) # Check if string starts with a specific character
print(str.capitalize()) # Capitalize the first character
print(str.strip()) # Remove leading and trailing whitespace
print(str.count("l")) # Count occurrences of a character
print(str.find("o")) # Find index of first occurrence of a character



# Conditional Statements - Used to perform different actions based on different conditions.
# if-elif-else statements
num = 10
if num > 0:
    print("Positive Number") 
    print("This is inside if block")  # Indentation is important in Python - it defines the scope of the block - all indented lines belong to the if block (Proper Spacing)
elif num == 0:
    print("Zero")
else:
    print("Negative Number")


# Nested if statements
num = 15
if num > 0:
    if num % 2 == 0:
        print("Positive Even Number")
    else:
        print("Positive Odd Number")
else:
    print("Negative Number")
    
