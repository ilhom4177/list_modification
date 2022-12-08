def remove_even(lst):
    '''Given a list of numbers, write a function that returns a new list where all the even numbers are removed.
    
    Args:
        lst (list): list of numbers.
        
    Returns:
        list: list without even numbers.
    '''
    remove_even = []
    for i in lst:
        if i%2==1:
            remove_even.append(i)

    return remove_even
print(remove_even([1,2,3,4,5]))