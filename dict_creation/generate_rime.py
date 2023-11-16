import os
from pathlib import Path
import pandas
from datetime import datetime

yaml_template = r'''
# Rime dictionary
# encoding: utf-16
# timestamp: %%TS%%
# author: Alan Xiang (ziyue.alan.xiang@gmail.com)

---
name: wubi98_optimized
version: "1.0.0"
sort: original
columns:
  - text
  - code
  - weight
  - stem
encoder:
  exclude_patterns:
    - '^z.*$'
  rules:
    - length_equal: 2
      formula: "AaAbBaBb"
    - length_equal: 3
      formula: "AaBaCaCb"
    - length_in_range: [4, 32]
      formula: "AaBaCaZa"
...
'''.strip()

yaml_template = yaml_template.replace('%%TS%%', datetime.now().isoformat())

my_dir = Path(os.path.dirname(__file__))
table_path = my_dir/'..'/'tables'/'ime_table.csv'
table_df = pandas.read_csv(table_path)
rime_dict_output = my_dir/'..'/'dictionaries'/'wubi98_opt.yaml'


# first of all, need to generate stem code for incomplete code
code_lut = dict()
for ind, row in table_df.iterrows():
    code_lut[row.output] = row.code


with open(rime_dict_output, 'w', encoding='utf16') as f:

    f.write(yaml_template + '\n')

    for gp_key, gp_df in table_df.groupby('code'):
        for item in gp_df.output:
            assert ' ' not in item, str(gp_df)
        
        group_size = gp_df.shape[0]


        for ind, item in enumerate(list(gp_df.output)):
            
            priority = group_size + 1 - ind

            gp_key_full = None
            if len(gp_key) < 4:
                gp_key_full = code_lut.get(item, None)

            if gp_key_full:
                f.write(f'{item}\t{gp_key}\t{priority}\t{gp_key_full}\n')
            else:
                f.write(f'{item}\t{gp_key}\t{priority}\n')

