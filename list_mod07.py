def square_and_remove_odd(lst):
    '''Given a list of numbers, write a function that returns a new list where all the numbers are squared and all the odd numbers are removed.
    
    Args:
        lst (list): list of numbers.
        
    Returns:
        list: list of all odd numbers are squared.
    '''
    s = []
    n = len(lst)
    for i in range(n):
        lst[i] = lst[i]**2
        if lst[i]%2==0:
            s.append(lst[i])
    return s
print(square_and_remove_odd([1, 3, 5]))