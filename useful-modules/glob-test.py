import glob

# py_files = [path for path in glob.glob('./*.py', )]
# for path in py_files:
#   print(path)

paths = 0
for path in glob.glob('/Users/<user>/Documents/work/**/*.sh', recursive=True):
  paths += 1

print(paths)