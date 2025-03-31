# Because of their immutability, tuples are a bit faster in python

print("\n       LISTS        \n")

my_list = [2, 4, 'word']

print(f"List: {my_list}   -->   Length: {len(my_list)}")

my_list.clear()

print(f"Cleared list: {my_list}   -->   Length: {len(my_list)}")

my_list = [2, 4, 'word']

others = [9, 8, 'X']

my_list.extend(others)

print(f"Extended list: {my_list}")

my_list.reverse()
print(f"Reversed list: {my_list}")

print("\n------------------------------\n")

print("\n       TUPLES        \n")

my_tuple = (2, 5.6, True, 'man', [3, 4, "woman"])

print(my_tuple)

print(f"my_tuple[3]: {my_tuple[3]}   my_tuple[-2]: {my_tuple[-2]}")

print("\n------------------------------\n")

print("\n       SLICING        \n")

test_list = [1, 2, 3, 4, 5, 6]

print(f"test_list: {test_list}\n")

print(f"test_list[1:1]  ->  {test_list[1:1]}")
print(f"test_list[1:2]  ->  {test_list[1:2]}")
print(f"test_list[1:3]  ->  {test_list[1:3]}")
print(f"test_list[:]  ->  {test_list[:]}")

print("\nPositive direction:")
print(f"test_list[1:6:1]  ->  {test_list[1:6:1]}")
print("I can omit the 6 to indicate to the end of the list:")
print(f"test_list[1::1]  ->  {test_list[1::1]}")

print("\nNegative direction with -1:")
print(f"test_list[1::-1]  ->  {test_list[1::-1]}")
print(f"test_list[2::-1]  ->  {test_list[2::-1]}")
print("reversed list:")
print(f"test_list[::-1]  ->  {test_list[::-1]}")

print("\nJumping:")
print(f"test_list[::2]  ->  {test_list[::2]}")
print(f"test_list[::-2]  ->  {test_list[::-2]}")

print("\n------------------------------\n")

print("\n       UNPACKING        \n")

a, b = (10, 5)

print(f"a, b = (10, 5)  -->  a = {a}, b = {b}")

print("\nI can create a tuple without brackets:")
items = 2, 4, 6
print(f"items = 2, 4, 6  -->  print(items)  -->  {items}")

print("\nSwitch values:")
value_1 = 10
value_2 = 'test'
print(value_1, value_2)
value_1, value_2 = value_2, value_1
print(value_1, value_2)
