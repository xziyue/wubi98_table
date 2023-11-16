import os
from pathlib import Path


my_dir = Path(os.path.dirname(__file__))

def read_code(filename, sep='\t'):
    ret = set()
    with open(filename, 'r', encoding='utf16') as f:
        for line in f:
            line = line.strip()
            if line:
                code = line.partition(sep)[0]
                ret.add(code)

    return ret


code1 = read_code(my_dir/'..'/'dictionaries'/'wubi98_multiple.txt', '\t')
code2 = read_code(my_dir/'..'/'predefined_dictionaries'/'wubi98_dict.txt', ' ')

union = code1.union(code2)
missing_code = union.difference(code1)

print(missing_code)