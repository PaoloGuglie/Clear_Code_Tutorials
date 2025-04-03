# Nested loops in list comprehensions:

pairs = [(1, 2), (3, 4), (5, 6)]

flattened = [num for pair in pairs for num in pair]

print(flattened)

# It's the same as:

flattened = []

for pair in pairs:
    for num in pair:
        flattened.append(num)

print(flattened)
