def remove_odd(lst):
    '''Given a list of numbers, write a function that returns a new list where all the odd numbers are removed.

    Args:
        lst (list): a list of number.
    
    Returns:
        list: list without odd numbers.
    '''
    even_list = []
    for i in lst:
        if i%2==0:
            even_list.append(i)

    return even_list
print(remove_odd([1, 2, 3, 4, 5]))