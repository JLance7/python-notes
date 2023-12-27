import os
import pathlib

# os.mkdir('test_dir')
# os.rmdir('test_dir')

# path = input('Enter path: ')
# if os.path.exists(path):
#   print(f'{path} exists')
# else:
#   print(f'{path} does not exist')

# print('What is the file in the current dir you want to get full path of?')
# file = input()
# if os.path.exists(os.path.abspath(file)):
#   print(os.path.abspath(file))

cwd = os.getcwd()
print(cwd)

os.chdir('..')
print(os.getcwd())

parent_dir = '/Users/c7g4q3/Documents'
directory = 'TPDE'
path = os.path.join(parent_dir, directory)
print(path)
print()
print(os.listdir(path))
# os.rmdir()

print(os.name)

try:
    filename = 'GFG.txt'
    f = open(filename, 'rU')
    text = f.read()
    f.close()
 
except IOError:
 
    print('Problem reading: ' + filename)

# pathlib

obj = pathlib.PurePath('/Users/c7g4q3/Documents/TPDE')
