import csv

fields = ['index', 'status', 'number']

with open('test.txt', 'r') as f:
  with open('csv_output.csv', 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)

    for line in f.readlines():
      index = line.split(' ')[0]
      status = line.split(' is a ')[1].split(' number')[0]
      number = line.split(' is a ')[1].split(status)[1].strip()
      
      csvwriter.writerow([index, status, number])

my_dict = [
  {'index': '101', 'status': 'prime', 'number': 'num'},
  {'index': '102', 'status': 'prime', 'number': 'num'},
  {'index': '103', 'status': 'prime', 'number': 'num'},
]

with open('csv_output.csv', 'a') as csvfile:
  csvwriter = csv.DictWriter(csvfile, fieldnames=fields)
  # csvwriter.writeheader()
  csvwriter.writerows(my_dict)