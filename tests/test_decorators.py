
def print_break():
    print "******************************************************************"

################################################################################
#define a global variable
top_str = "I am a global variable"
def foo():
    print top_str


def foo_a():
    #only modifies a local copy of a_str
    top_str = "something different"
    print top_str


foo()
foo_a()


print top_str
print_break()
################################################################################
# example of functions inside functions


def outside():
    x = 10
    # definition of inside function
    def inside():
        print "inside:",x
    inside()


outside()
# inside is not in scope
#inside()

print_break()
################################################################################
# functions as object

def add(x, y):
    return x + y

def mul(x, y):
    return x * y

def run_func(func, x, y):
    return func(x, y)

a = 10
b = 12
print "mul:",a,b,":",run_func(mul, a, b)
print "add:",a,b,":",run_func(add, a, b)


print_break()
################################################################################
# function closures

def outer(x, y=None):
    def inner():
        print x
        print y
    return inner

p1 = outer(1)
p2 = outer(2)

print p1.func_closure
print p2.func_closure
p1()
p2()

print_break()

################################################################################
# decorators

def safety(func):
    def bounds_checker(a, b):

        if (a < 0):
            a = 0
        if (b < 0):
            b = 0
        ret = func(a, b)
        return ret
    return bounds_checker


def unsafe_add(a, b):
    return a + b

# decorator same as
#safe_add = safety(safe_add)
@safety
def safe_add(a, b):
    return a+b

a = -1
b = 12
print "unsafe_add:",a,b,unsafe_add(a, b)
print "safe_add:",a,b,safe_add(a, b)


