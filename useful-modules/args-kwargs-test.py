def test_args(arg_1, *args):
  print(arg_1)
  for arg in args:
    print(arg)

test_args('one', 'two', 'three', 'four', 'five')


def greet_me(**kwargs):
  for key, value in kwargs.items():
    print("{0} = {1}".format(key, value))

greet_me(name="Josh", age=22)

def print_args_kwargs(arg1, arg2, arg3):
  print(arg1)
  print(arg2)
  print(arg3)

args = ["one", 2, 3]
print_args_kwargs(*args)
kwargs = {"arg1": "wow", "arg2": "cool", "arg3": "awesome"}
print()
print_args_kwargs(**kwargs)

print()
def using_both(*args, **kwargs):
  if args:
    for arg in args:
      print(arg)
  
  if kwargs:
    for key, val in kwargs.items():
      print(f'{key} = {val}')

using_both('one', 'two', 'three', 'four', 'five', name='Josh', age=22)