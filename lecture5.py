# Loops in Python
# This script demonstrates the use of loops in Python 
# including 'for' loops and 'while' loops.

# For Loop Example
print("For Loop Example:")
for i in range(5):
    print(f"Iteration {i + 1}")
print("\n")



# While Loop Example
print("While Loop Example:")
count = 0
while count < 5:
    print(f"Count is {count}")
    count += 1
print("\n")



# Nested Loop Example
print("Nested Loop Example:")
for i in range(3):
    for j in range(2):
        print(f"Outer loop iteration {i + 1}, Inner loop iteration {j + 1}")
print("\n")



# Loop with Break and Continue
print("Loop with Break and Continue:")
for num in range(10):
    if num == 5:
        print("Breaking the loop at 5")
        break
    if num % 2 == 0:
        print(f"Skipping even number: {num}")
        continue
    print(f"Processing number: {num}")
print("\n")



#for else
name = "Ankan"
for ele in name :
    print(ele) 
else :
    print("Ghorai")




# while else
count = 0
while count < 3 :
    print(count)
    count += 1
else :
    print("Loop ended")




# range(start, stop, step) function
print(range(5))  # Outputs: range(0, 5)
print("Range Function Example:")
for num in range(2, 10, 2):
    print(num)
print("\n")



# Infinite Loop Example (Commented out to prevent execution)
# print("Infinite Loop Example:")
# while True:
#     print("This will run forever unless stopped manually.")


# pass statement in loops
print("Pass Statement Example:")
for i in range(5):
    if i == 3:
        pass  # Placeholder for future code
    print(i)
print("\n")



