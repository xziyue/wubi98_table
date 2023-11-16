import os
from pathlib import Path
import pandas

my_dir = Path(os.path.dirname(__file__))

table_path = my_dir/'..'/'tables'/'ime_table.csv'

table_df = pandas.read_csv(table_path)

single_output = my_dir/'..'/'dictionaries'/'wubi98_single.txt'
multiple_output = my_dir/'..'/'dictionaries'/'wubi98_multiple.txt'

# generate single
with open(single_output, 'w', encoding='utf16') as f:
    for ind, row in table_df.iterrows():
        f.write(f'{row.code}\t{row.output}\n')

# generate multiple
with open(multiple_output, 'w', encoding='utf16') as f:
    for gp_key, gp_df in table_df.groupby('code'):
        for item in gp_df.output:
            assert ' ' not in item, str(gp_df)
        outputs = '\t'.join(gp_df.output)
        f.write(f'{gp_key}\t{outputs}\n')



single_rev_output = my_dir/'..'/'dictionaries'/'wubi98_single_reverse.txt'

# generate single
with open(single_rev_output, 'w', encoding='utf16') as f:
    for gp_key, gp_df in table_df.groupby('code'):
        for item in gp_df.output:
            assert ' ' not in item, str(gp_df)

        for item in reversed(list(gp_df.output)):
            f.write(f'{gp_key}\t{item}\n')

