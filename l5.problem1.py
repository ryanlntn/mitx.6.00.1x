def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    total = 1
    for i in range(exp):
        total *= base
    return total
