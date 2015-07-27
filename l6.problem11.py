def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    biggest_key = None
    biggest_value = 0
    for key, value in aDict.iteritems():
        if len(value) >= biggest_value:
            biggest_key = key
            biggest_value = len(value)
    return biggest_key
