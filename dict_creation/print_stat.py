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

print('num ch.', num_ch)
print('num word', num_word)
