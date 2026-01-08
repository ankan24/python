# File Input/Output in Python
# This script demonstrates how to read from and write to files in Python.
# It covers opening files, reading content, writing content, and closing files.

# Python can be used to perform operations on a file (read & write data)
# There are two types of files:
# 1. Text files (.txt, .docx, .log etc.)
# 2. Binary files (.bin, .jpg, .png, .mp4 etc.)

# Opening a file
# 'r' - Read mode (default)
# 'w' - Write mode (creates a new file or truncates an existing file)
# 'a' - Append mode (adds data to the end of the file)
# 'b' - Binary mode (used for binary files)
# 't' - Text mode (default, used for text files)
# 'x' - Exclusive creation (creates a new file, fails if the file exists)
# 'r+' - Read and write mode (pointer start at the beginning of the file)
# 'w+' - Write and read mode (truncates existing file or creates a new one)
# 'a+' - Append and read mode (pointer at end of file)
# '+' - Update mode (read and write)
# Example: Open a text file in write mode

# Reading from a file
file = open("example.txt", "r")  # Open the file in read mode
content = file.read()  # Read the entire content of the file
content0 = file.read(10)  # Read the first 10 characters from the file
content1 = file.readline()  # Read a single line from the file
content2 = file.readlines()  # Read all lines into a list
print("File Content:\n", content)  # Print the content read from the file
file.close()  # Close the file after reading


# Writing to a file
file = open("example.txt", "w")  # Open a file named example.txt in write mode
file.write("Hello, World!\n")  # Write a line to the file
file.write("This is a sample file.\n")
file.close()  # Always close the file after operations

# Appending to a file
file = open("example.txt", "a")  # Open the file in append mode
file.write("Appending a new line to the file.\n")  # Append a new line
file.close()  # Close the file after appending


# Creating a new file
f = open("sample.txt", "x")  # Create a new file named sample.txt
f.close()  # Close the file



# Using 'with' statement for file operations
# This automatically handles closing the file
with open("example.txt", "r") as f:
    data = f.read()
    print("File Content using 'with':\n", data)

# Deleting a file
# using the os module
import os
os.remove("sample.txt")  # Delete the file named sample.txt

# pip install os-sys # to install os module if not already installed