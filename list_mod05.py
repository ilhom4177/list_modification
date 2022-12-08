def square(lst):
    '''Given a list of numbers, write a function that returns a new list where all the numbers are squared.
    
    Args:
        lst (list): list of numbers.
        
    Returns:
        list: list of all numbers are squared.
    '''

    n = len(lst)
    for i in range(n):
        lst[i] = lst[i]**2
    return lst
print(square([1,2,3,4,5]))