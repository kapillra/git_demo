def add(x, y, *numbers):
    '''this is a function
    to add multiple numbers.'''
    
    ## new
    
    s = x + y
    for i in numbers:
        s += i
    return s