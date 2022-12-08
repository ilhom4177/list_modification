def square_and_remove_even(lst):
    '''Given a list of numbers, write a function that returns a new list where all the numbers are squared and all the even numbers are removed.
    
    Args:
        lst (list): list of numbers.
        
    Returns:
        list: list of all even numbers are squared.
    '''
    s = []
    n = len(lst)
    for i in range(n):
        lst[i] = lst[i]**2
        if lst[i]%2==1:
            s.append(lst[i])
    return s
print(square_and_remove_even([1, 2, 3, 4, 5]))