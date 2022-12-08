# list_modification

# Problems

## Problem 1

Given a list of numbers, write a function that returns a new list where all the odd numbers are removed.

**Example 1:**

```python
>>> remove_odd([1, 2, 3, 4, 5])
[2, 4]
```

**Example 2:**

```python
>>> remove_odd([1, 3, 5])
[]
```

## Problem 2

Given a list of numbers, write a function that returns a new list where all the even numbers are removed.

**Example 1:**

```python
>>> remove_even([1, 2, 3, 4, 5])
[1, 3, 5]
```

**Example 2:**

```python
>>> remove_even([2, 4, 6])
[]
```

## Problem 3

Given a list of numbers, write a function that returns a new list where all the negative numbers are removed.

**Example 1:**

```python
>>> remove_negative([1, -2, 3, -4, 5])
[1, 3, 5]
```

**Example 2:**

```python

>>> remove_negative([-1, -3, -5])
[]
```

**Example 3:**

```python

>>> remove_negative([-1, -3, 0])
[0]
```

## Problem 4

Given a list of numbers, write a function that returns a new list where all the positive numbers are removed.

**Example 1:**

```python

>>> remove_positive([1, -2, 3, -4, 5])
[-2, -4]
```

**Example 2:**

```python
>>> remove_positive([1, 3, 5])
[]
```

**Example 3:**

```python
>>> remove_positive([1, 3, 5, 0])
[0]
```

## Problem 5

Given a list of numbers, write a function that returns a new list where all the numbers are squared.

**Example 1:**

```python
>>> square([1, 2, 3, 4, 5])
[1, 4, 9, 16, 25]
```

**Example 2:**

```python

>>> square([2, 4, 6])
[4, 16, 36]
```

## Problem 6

Given a list of numbers, write a function that returns a new list where all the numbers are squared and all the even numbers are removed.

**Example 1:**

```python
>>> square_and_remove_even([1, 2, 3, 4, 5])
[1, 9, 25]
```

**Example 2:**

```python
>>> square_and_remove_even([2, 4, 6])
[]
```

## Problem 7

Given a list of numbers, write a function that returns a new list where all the numbers are squared and all the odd numbers are removed.

**Example 1:**

```python

>>> square_and_remove_odd([1, 2, 3, 4, 5])
[4, 16]
```

**Example 2:**

```python

>>> square_and_remove_odd([1, 3, 5])
[]
```

## Problem 8

Given a list of numbers, write a function that returns a new list where all the numbers are squared and all the negative numbers are removed.

**Example 1:**

```python
>>> square_and_remove_negative([1, -2, 3, -4, 5])
[1, 9, 25]
```

**Example 2:**

```python
>>> square_and_remove_negative([-1, -3, -5])
[]
```

**Example 3:**

```python
>>> square_and_remove_negative([-1, -3, 0])
[0]
```

## Problem 9

Given a list of numbers, write a function that returns a new list where all the numbers are squared and all the positive numbers are removed.

**Example 1:**

```python
>>> square_and_remove_positive([1, -2, 3, -4, 5])
[4, 16]
```

**Example 2:**

```python
>>> square_and_remove_positive([1, 3, 5])
[]
```

```python
>>> square_and_remove_positive([1, 3, 0])
[0]
```

## Problem 10

Given a list of numbers, write a function that returns a new list where all the numbers are squared and all the numbers that are divisible by 3 are removed.

**Example 1:**

```python

>>> square_and_remove_divisible_by_3([1, 2, 3, 4, 5])
[1, 4, 16, 25]
```

**Example 2:**

```python
>>> square_and_remove_divisible_by_3([3, 6, 9])
[]
```

## Problem 11

Given a list of numbers, write a function that returns a new list where all the maximum numbers are removed.

**Example 1:**

```python
>>> remove_max([1, 2, 3, 4, 5])
[1, 2, 3, 4]
```

**Example 2:**

```python
>>> remove_max([1, 2, 0, 3, 3])
[1, 2, 0]
```

**Example 3:**

```python
>>> remove_max([5, 5, 5])
[]
```

## Problem 12

Given a list of numbers, write a function that returns a new list where all the minimum numbers are removed.

**Example 1:**

```python

>>> remove_min([1, 2, 3, 4, 5])
[2, 3, 4, 5]
```

**Example 2:**

```python

>>> remove_min([2, 3, 2, 1, 1, 0])
[2, 3, 2, 0]
```

**Example 3:**

```python

>>> remove_min([1, 1, 1])
[]
```

## Problem 13

Given the list of numbers, Replace the maximum numbers in the list with 0.

**Example 1:**

```python

>>> replace_maximum_with_0([1, 2, 3, 4, 5])
[1, 2, 3, 4, 0]
```

**Example 2:**

```python

>>> replace_maximum_with_0([1, 2, -1, 0, 3, 3, 3])
[1, 2, -1, 0, 0, 0, 0]
```

## Problem 14

Given the list of numbers, Replace the mininum numbers in the list with 0.

**Example 1:**

```python

>>> replace_minimun_with_0([1, 2, 3, 4, 5])
[0, 2, 3, 4, 5]
```

**Example 2:**

```python

>>> replace_minimun_with_0([1, 2, -1, 0, 3, -1])
[1, 2, 0, 0, 3, 0]
```
