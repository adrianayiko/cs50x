#using extensions to a class in another class
def my_decorator(func):
    def wrapper():
        print("I am a decorator")

@my_decorator
def say_hello():
    print("Hello")
say_hello()