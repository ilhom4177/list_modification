def remove_positive(lst):
    '''Given a list of numbers, write a function that returns a new list where all the positive numbers are removed.
    
    Args:
        lst (list): list of numbers.
        
    Returns:
        list: list without positive numbers.
    '''
    l = []
    for i in lst:
        if i<0:
            l.append(i)

    return l
print(remove_positive([1, -2, 3, -4, 5]))