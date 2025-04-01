# Duplicates in sets are deleted

my_set = {1, 2, 2, 1, 3}

print(my_set)

my_set.add(13)
my_set.add(5)
my_set.add(8)

# Sets are NOT ordered, but they may appear as such when
# adding small integers. There is no guarantee of order.

my_set.remove(2)

print(my_set)

print("\n-------------\n")

# Indexing and slicing does not work

try:
    print(my_set[2])

except TypeError:
    print("No indexing!")

print("\n-------------\n")

print(my_set.pop())
print(my_set)

print("\n-------------\n")

# Get an item from a set
print(list(my_set)[2])

print("\n-------------\n")

# Sets are very good for comparisons.
# There are a lot of ways to check if 2 sets have
# values in commmon (or if they differ).

# set1.union(set2)  -->  creates a new set with shared elements

# set1.intersection(set2)  -->  creates a new set with elements present in both sets.

set1 = {1, 2, 3, 6, 6, 7}
set2 = {3, 4, 5, 6, 7}

print(f"Union: {set1.union(set2)}")
print(f"Intersection: {set1.intersection(set2)}")

print("------")

# Other way to get an .union()
print(f"Union: {set1 | set2}")

# Other way to get an .intersection()
print(f"Intersection: {set1 & set2}")

print("------")

# Difference
print(f"Difference: {set1 - set2}")  # A \ B  "elements of A that are not in B"

print("\n-------------\n")

# Find if a long list has duplicates

long_list = [i for i in range(1000)]
long_list.append(345)
long_list.append(212)
long_list.append(578)

list_length = len(long_list)
set_length = len(set(long_list))

if list_length > set_length:
    print(f"The original list has {list_length - set_length} duplicates!")

else:
    print("The original list has not duplicates!")
