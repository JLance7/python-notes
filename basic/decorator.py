import time

# pass func as arg
def say_hi(val):
  print(f'hi {val}')

def take_func(func, val):
  return func(val)

take_func(say_hi, 'Bob')

# inner func
def parent():
  def stuff():
    print('stuff')
  
  def inner_func():
    return 'hi'
  
  stuff()
  return inner_func

inner = parent()
print(inner())

print('-' * 10)
# decorator
# decorators wrap a function, modifying its behavior.
def my_dec(func):
  def wrapper():
    print('before')
    func()
    print('after')
  return wrapper

def say_hi():
  print('hi')

say_hi = my_dec(say_hi)
say_hi()
print('-' * 10)

# better way
def decor(funct):
  def wrapper():
    start_time = time.time()
    funct()
    end_time = time.time() - start_time
    print(f'took: {end_time} seconds')
  return wrapper

@decor
def testing():
  print('testing 1')
  time.sleep(0.5)
  print('testing 2')
  time.sleep(0.5)
  print('testing 3')
  time.sleep(0.5)

testing()

def do_twice(func):
  def wrapper(*args, **kwargs):
    func(*args, **kwargs)
    func(*args, **kwargs)
  return wrapper

@do_twice
def greet(name):
  print(f'hi {name}')

greet('Josh')

print('-' * 10)

# real world example
import functools

def decorator(func):
  @functools.wraps(func) # so __name__ isn't weird
  def wrapper(*args, **kwargs):
    print('do something before')
    val = func(*args, **kwargs)
    print('something after')
    return val
  return wrapper

def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer

@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])