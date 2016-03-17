#!/usr/bin/python

# example to show how to use generators

# define a method to create evens
def get_evens(max_num):
    for i in xrange(max_num+1):
        if i % 2 == 0:
            yield i

# call function with an upper limit
for val in get_evens(10):
    print val


# another way to call generators, keep calling until StopIteration
# exception is thrown
fp = get_evens(5)
try:
    while True:
        print next(fp)

except StopIteration as e:
    print e

print "done"
