import json

def parse(path):
    with open(path) as f:
        ipynb = json.load(f)
    py_cells = [item['source'] for item in ipynb['cells'] if item['cell_type']=='code' ]
    code = []
    for cell in py_cells:
        for x in cell:
            code.append(x)
    tmp_code_path = 'code_tmp.py'
    with open(tmp_code_path, 'w') as f:
        for line in code:
            if line.startswith('%') or \
                line.startswith('help('):
                continue
            f.write(line + '\n')
    return tmp_code_path