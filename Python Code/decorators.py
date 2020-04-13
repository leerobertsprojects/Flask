from time import time
import colorama



def hello():
    return "Hi Lee"


def other(func):
    print("some other code")
    func()
    print(func())


#other(hello)

# decorator
def new_decorator(func):
    def wrap_func():
        print("some code before executing func")
        print(time())
        func()
        print(time())
        print("Code here, after executing func()")
    return wrap_func

@new_decorator
def func_needs_dec():
    print("Please decorate me")


func_needs_dec()



