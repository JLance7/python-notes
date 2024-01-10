add_one = lambda x: x + 1
print(add_one(5))

def stuff(x, y):
  print('doing stuff')
  inner_func = lambda x, y: x + y
  result = inner_func(x, y)
  print(result)

stuff(5, 6)

full_name = lambda first, last: f'{first} {last}'
print(full_name('Josh', 'Sullivan'))

high_ord_func = lambda x, func: x + func(x)
print(high_ord_func(2, lambda x: x * x))

test = (lambda x:
        x + 2)

print(test(1))

summing = lambda *args: sum(args)
print(summing(1, 2, 3, 4, 5))

# higher order functions
"""
Map
Map applies a function to all the items in an input_list. Here is the blueprint:
map(function_to_apply, list_of_inputs)
"""
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))
print(squared)

"""
Filter
As the name suggests, filter creates a list of elements for which a function returns true. Here is a short and concise example:
filter(function, inputs)
"""
greater_than_two = list(filter(lambda x: x > 2, items))
print(greater_than_two)

"""
Reduce
Reduce is a really useful function for performing some computation on a list and returning the result. 
It applies a rolling computation to sequential pairs of values in a list. For example, if you wanted to compute the product of a list of integers.
"""
from functools import reduce
product = reduce((lambda x, y: x * y), [1, 2, 3, 4])


def return_greater_than_x(x, **kwargs):
  filtered = { k: v for k, v in kwargs.items() if v > x }
  return filtered

print(return_greater_than_x(2, a=1, b=2, c=3, d=4, e=5, f=6))