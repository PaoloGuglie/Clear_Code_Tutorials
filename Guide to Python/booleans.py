# In python there are Truthy and Falsy values.
# Truthy values are converted to True.
# Falsy values are converted to False.

# Falsy values: 0, 0.0, '', [], (), {}, None
# Truthy values: any other value

# bool() function can accept any value. It evaluates if a value is Truthy or Falsy:

print(f"bool is {bool(bool)}")

print(f"1 is {bool(1)}")

print(f"0.0 is {bool(0.0)}")

print(f"0.000000001 is {bool(0.000000001)}")

print(f"not True is {bool(not True)}")

print(f"None is {bool(None)}")
