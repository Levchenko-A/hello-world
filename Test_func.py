def test(a):
    '''returns list of a squares starting from zero
        and up to "a"'''
    b = [i ** 2 for i in range(a)]
    return b
#string added to test branching and merging
print('This is a new string in the file')
print(test(9))
