#using extensions to a class in another class
def my_decorator(func):#takes a function as an argument and returns a new function
    def wrapper():
        print("I am about to decorate the Function")
        func()
        print("Done with the function")
    return wrapper

@my_decorator
def hello():
    print("Hello")
hello()