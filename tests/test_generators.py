#!/usr/bin/python


# example to show how to use generators

def print_bar():
    print "===================================================================="

# define a method to create evens
def get_evens(max_num):
    for i in xrange(max_num+1):
        if i % 2 == 0:
            yield i


# define a method to create a value, and read a value
# from send method
def get_power(power):
    base = 0
    while True:
        base = yield base
        base = base ** power


# call function with an upper limit
print_bar()
print "print even numbers using a generator method in a for loop"
for val in get_evens(10):
    print val


# another way to call generators, keep calling until StopIteration
# exception is thrown
print_bar()
print "print event numbers using a generator method in a try catch"
fp = get_evens(5)
try:
    while True:
        print next(fp)
except StopIteration as e:
    print e


print_bar()
print "print values raised to the power of 3 using generator/send"
# example to show how to send a value to a generator function
power_fp = get_power(3)

#first start the generator
power_fp.send(None)
print power_fp.send(10)
print power_fp.send(4)
print power_fp.send(2)

print "done"
