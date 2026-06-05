def my_decorator(func):
    def wrapper():
        print("Preparing the pizza base...")
        func()
        print("Adding extra toppings...")
    return wrapper

@my_decorator
def my_func():
    print("Plain Pizza is ready!")

my_func()

# output
# Preparing the pizza base...
# Plain Pizza is ready!
# Adding extra toppings...
