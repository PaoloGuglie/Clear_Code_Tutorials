# I can also create tuple, dict and set comprehensions:

print("------------------------\n")

print("TUPLE COMPREHENSION", end=': ')
tuple_comp = tuple(i for i in range(10))

print(tuple_comp)

print("\n-------------------------\n")

print("SET COMPREHENSION", end=': ')
set_comp = {i for i in range(10)}

print(set_comp)

print("\n-------------------------\n")

print("DICTIONARY COMPREHENSION", end=': ')
dict_comp = {i: i for i in range(10)}

print(dict_comp)

print("\n-------------------------\n")

print("SQUARES", end=': ')
print({i: i**2 for i in range(1, 11)})

print("\n-------------------------\n")

print("EXERCISE", end=': ')
exercise_comp = {letter: value for letter, value in zip('ABCDE', [1, 2, 3, 4, 5])}
print(exercise_comp)