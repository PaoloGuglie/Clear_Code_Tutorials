# The .strip() method looks at the right and left side of a word and removes
# a certain kind of values

username = 'JOhn SmIthXX'.title().strip('x')  # use lowercase x because of .title()

print(username)


# To learn the methods (dunder and normal) available to something:
print(dir(username))

print(username.isalpha())  # returns False because of the space ' ' in the name

exercise_string = 'I like puppies puppies puppies'.replace('puppies', 'kittens')
# (I can also have as a third argument the number of times to replace the string)

print(exercise_string)
