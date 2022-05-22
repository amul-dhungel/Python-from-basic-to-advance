# Errors and exception
class ExceptionExample:
# this is way of creating of exception error
    x = -5
    if x < 0:
        raise Exception('x should be positive')


    # instead of if , you can use assert
    assert(x>=0), 'x is not positive'

    # using of try-exception block
    try:
        a =   5 / 0
    except ZeroDivisionError as e:
        print(e)
    except TypeError as e:
        print(e)
    else:
        print("success, no errors are found")
    finally:
        print("cleaning up....")


# class based way of creating 
# this is of creating your own class exception
class ValueTooHighError(Exception):
    pass

class ValueTooSmall(Exception):
    def __init__(self,message,value):
        self.message = message
        self.value = value
    

def test_value(x):
    if x > 100:
        raise ValueTooHighError('value is too high')
    if x < 100:
        raise ValueTooSmall('value too small',x)


# creating of try-except block
try:
    test_value(1)
except ValueTooHighError as e:
    print(e)
except ValueTooSmall as e:
    print(e.message,e.value)
