# Manual file opening and closing:

file = open('test.txt')

print(file)
print("------------")
for i in file: print(i)

file.close()

print("\n---------------------\n")


# Automatic file opening:

with open('test.txt', 'r') as file:
    # one way to open the file
    for i in file: print(i)
    # other method to print data
    print(file.read())

print("\n---------------------\n")


# Write something ("w" is to replace text, "a" is to append text):

with open('test.txt', 'a') as file:
    file.write('\nAAAAAAAAA')

print("\n---------------------\n")


# Create a new file (using a filename not already taken):

with open('other_text.txt', 'w') as file:
    file.write('This is another test file')
