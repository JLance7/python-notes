f = open('test.txt', 'w')
for i in range(100):
  f.write(f'{i+1} is a cool number\n')
f.close()

with open('test.txt', 'r') as f:
  for line in f.readlines():
    print(line, end='')