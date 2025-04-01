# This:
x = 0
while x < 5:
    x += 1
    print(x, end=' ')

print("\n-------------")

# is the same as:
x = 0
while x < 5: x += 1; print(x, end=' ')

print("\n-------------")


# Python has a special way to use if statements on a single line.
# It is the ternary operator:

x = 6

color = 'blue' if x < 5 else 'red'
print(color)

print("-------------")

a = ['blue' if x < 5 else 'red', 'yellow' if x % 2 == 0 else 'green']
print(a)
