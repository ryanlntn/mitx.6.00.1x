def oddTuples(aTup):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup.
    '''
    return tuple(x for i, x in enumerate(aTup) if i % 2 == 0)
