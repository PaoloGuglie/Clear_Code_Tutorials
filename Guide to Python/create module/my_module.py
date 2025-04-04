test_var = 'test'


def test_function(content):
    print(f'\nThis is an imported function with the parameter: {content}')


class MyClass:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __call__(self):
        print(f"\nHello, my name is {self.name} and my value is {self.value}")


print(f"\nImported file: {__name__}")

print("\n------------------------\n")
