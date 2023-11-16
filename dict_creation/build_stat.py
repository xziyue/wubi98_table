import os
from pathlib import Path
import pandas

my_dir = Path(os.path.dirname(__file__))

table_path = my_dir/'..'/'tables'/'ime_table.csv'

table_df = pandas.read_csv(table_path)

ch_set = set()
for v in table_df.output:
    ch_set.add(v)

num_ch = 0
num_word = 0

for item in ch_set:
    if len(item) == 1:
        num_ch += 1
    else:
        num_word += 1

with open(my_dir/'README.md', 'w') as f:
    f.write(f'- Number of characters: {num_ch}\n')
    f.write(f'- Number of words/phrases: {num_word}\n')
