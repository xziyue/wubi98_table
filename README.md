# Building Wubi 98 Dictionaries

Generated dictionaries are in [dictionaries/](dictionaries/).

## Procedure

Install Python dependencies using [requirements.txt](requirements.txt).

### Collecting IME table

1. Run [code_collection/collector.py](code_collection/collector.py) to collect input-output mapping table from an IME
2. Run [code_collection/record_sanitizer.py](code_collection/sanitizer.py) to aggregate and sanitize the output of `collector.py`; this will generate [tables/ime_table.csv](tables/ime_table.csv)


### Converting IME table to other formats

The generated dictionaries will be stored in [dictionaries/](dictionaries/).

- [dict_creation/generate_simple.py]([dict_creation/generate_simple.py): generate simple one mapping per line/multiple mapping per line dictionaries
