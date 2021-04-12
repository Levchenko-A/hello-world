def test(a):
    '''returns list of a squares starting zero
        and up to "a"'''
    b = [i ** 2 for i in range(a)]
    return b


print(test(8))
