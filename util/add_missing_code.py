import os
from pathlib import Path
import itertools
import string
import json

my_dir = Path(os.path.dirname(__file__))

def read_code(filename, sep='\t'):
    lut = dict()
    with open(filename, 'r', encoding='utf16') as f:
        for line in f:
            line = line.strip()
            if line:
                code, _, word = line.partition(sep)
                if code in lut:
                    lut[code].append(word)
                else:
                    lut[code] = [word]

    return lut


# letters = string.ascii_lowercase[:-1]
# all_code = []
# for code_len in [1,2,3,4]:
#     for item in itertools.product(letters, repeat=code_len):
#         all_code.append(''.join(item))

# code3 = set(all_code)

lut1 = read_code(my_dir/'..'/'dictionaries'/'wubi98_multiple.txt', '\t')
lut2 = read_code(my_dir/'..'/'predefined_dictionaries'/'wubi98_dict.txt', ' ')

code1 = set(lut1.keys())
code2 = set(lut2.keys())

union = code1.union(code2)
missing_code = union.difference(code1)
#missing_code_2 = code3.difference(union)


for code in missing_code:
    print(lut2[code])

# print()
# print(missing_code_2)

# with open(my_dir/'missing_code.json', 'w') as f:
#     json.dump(list(missing_code), f)