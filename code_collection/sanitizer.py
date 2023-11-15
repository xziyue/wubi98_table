import os
from pathlib import Path
import string
import pandas

my_dir = Path(os.path.dirname(__file__))

record_files = my_dir.glob('record_*')


exclude_keys = []

ime_table = dict()

for fn in record_files:
    with open(fn, encoding='utf8') as f:
        for line in f:
            line = line.strip()
            if line:
                line_fields = line.split(' ')
                code = line_fields[0]
                index = line_fields[1]
                output = ' '.join(line_fields[2:])
                if output[-1] in string.digits:
                    continue
                if ' ' in output:
                    print(f'skipped {code} "{output}"')
                    continue

                index = int(index)
                key = (code, index)
                if key in exclude_keys:
                    continue

                if key in ime_table:
                    assert output == ime_table[key], 'incompatible input-output map'
                else:
                    ime_table[key] = output


# need to merge with single
single_lut = dict()
with open(my_dir/'wubi98_single.txt', encoding='utf16') as f:
    for line in f:
        line = line.strip()
        if line:
            ch, code = line.split('\t')
            single_lut[ch] = code


single_insert_index = 7

all_ch = set()
for v in ime_table.values():
    all_ch.add(v)

for ch, code in single_lut.items():
    if ch not in all_ch:
        ime_table[(code, single_insert_index)] = ch

all_kv = [(k1, v1, v) for (k1, v1), v in ime_table.items()]
all_kv.sort(key=lambda x : x[:2])

code, sel_index, output = list(zip(*all_kv))

df = pandas.DataFrame({'code': code, 'sel_index': sel_index, 'output': output})
df.to_csv(my_dir/'..'/'tables'/'ime_table.csv', index=None)