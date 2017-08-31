#/usr/bin/python



def throw_and_hide():
    try:
        str = "hello"

        print str[8]

        fh = open("non-existant")
        print fh.readlines()

        pass
    except Exception as e:
        print "exception caught"
        print e


def throw_custom_and_hide():
    try:
        raise Exception("this is a custom message")
    except Exception as e:
        print "exception caught in throw_custom_and_hide"
        print e

if __name__ == "__main__":
    throw_and_hide()
    throw_custom_and_hide()

