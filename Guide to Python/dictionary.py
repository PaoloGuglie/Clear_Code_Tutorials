my_dict = {
    'key': 'value',
    1: [3, 5],
    'name': {
        3.423: False
    }
}

# Convert a dict
print(list(my_dict), tuple(my_dict))
print(list(my_dict.items()))

print("\n---------\n")

# Get items
print(my_dict['name'])
print(my_dict.get(1))

# get() is considered better because it does not give an error when it cannot
# find a key. It returns None in that case.

print("\n---------\n")

# Update dictionary
my_dict.update({'other': ('1', 1)})
my_dict.update(WHAT='TF', text=34)

my_dict['S'] = 100

print(my_dict)
