def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    if len(aStr) > 1:
        m_index = len(aStr) / 2
        middle = aStr[m_index]
    else:
        return char == aStr

    if char == middle:
        return True
    elif char < middle:
        return isIn(char, aStr[0:m_index])
    else:
        return isIn(char, aStr[m_index:])
