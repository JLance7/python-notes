import time
import random
from dotenv import load_dotenv
import os

load_dotenv()
aws_prof = os.getenv('AWS_PROFILE')
print(aws_prof)
# printing method one
var1 = 'hi'
var2 = 'Jim'
print(str(var1) + ' there ' + str(var2))
# printing method 2
print('f{var1} there {var2}')
# method 3
print('%s there %s' % (var1, var2))
# method 4
print('this is {status}'.format(status='awesome'))

# make random number between two numbers inclusive and time the code
start_time = time.time()
starting = 1
ending = 4
num = random.randint(starting, ending)
print(f'random num: {num}')

end_time = time.time() - start_time
end_time_min = end_time / 60
if end_time_min < 1: end_time_min = 0
end_time_sec = end_time % 60
print('It took {:02}:{:02} seconds to run this code'.format(end_time_min, end_time_sec))