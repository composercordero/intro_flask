def my_decorator(func):
    def wrapper():
        print('this is happening before the function is called')
        func()
        print('this is happening after the function is called')
    return wrapper

def say_hello():
    print('Hello, How are you today?')

say_hello = my_decorator(say_hello)

say_hello()

print('-'*100)

@my_decorator
def say_goodbye():
    print('goodbye')

say_goodbye()

from test import format_name

print(format_name('carlos', 'cordero'))
