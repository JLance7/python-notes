## Pandas dataframe
.loc['row_index_name'] for getting row
.loc['row_index_name', 'col'] for getting specific item from row

index based [row, col]
.iloc[row_index] retrieve row
.iloc[:, col_index] retrieve all rows of col]
.at[] for signular rows/cols

df.fillna(0) fill nan with 0
df.dropna() drop rows will null values

filtering
df[df['column'] == 'val'] returns all rows where col == val

df['col_name'] to select single column
df[['col_1', 'col_2']] to select multiple columns

for index, row in enumerate(df.itertuples()):
  row.col = 1

try:

except blank_error:
  raise


pip install -e . # editable mode

Libraries
  • os, platform, pathlib
  • logger
  • configparser
  • pandas, numpy, matplotlib, seaborn
  • requests, urllib3
  • argparse
  • time for timing code
  • re for regular expression
  • glob for returning list of paths that match pattern
  • csv
  • unittest
  • openpyxl to use pd.ExcelWriter() to save multiple sheets to excel file

with pd.ExcelWriter('output.xlsx') as writer: 
  df1.to_excel(writer, sheet_name='Sheet_name_1') 
  df2.to_excel(writer, sheet_name='Sheet_name_2')

debugging cli
$ python -m pdb my_script.py

to build package do: python setup.py sdist
