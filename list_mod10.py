def square_and_remove_divisible_by_3(lst):
    '''Given a list of numbers, write a function that returns a new list where all the numbers are squared and all the numbers that are divisible by 3 are
    
    Args:
        lst (list): list of numbers.
    
    Returns:
        list: list of all numbers are not divisible by 3.
    '''
    list1=[]
    for i in range(len(lst)):
        if lst[i]%1!=0:
            x=lst[i]**2
            list1.append(x)
    return list1
print(square_and_remove_divisible_by_3([3, 6, 9]))