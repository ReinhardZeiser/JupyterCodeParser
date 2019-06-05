# JupyterCodeParser
Simple module to extract/run code written in a Jupyter Notebook.  
  
**Usecase:** 
- extracting code after prototyping in Jupyter
- program in Jupyter for better documentations and always run your code with run_ipynb.py 

## parse_ipynb
Parses code from Jupyter file (\*.ipynb) and writes it to outputfile.  
  

Use *# omit cell* in the beginning of a code-cell, to prevent adding the content of this cell to the outputfile.
```python 
  # omit cell
  print('This code will not be in the outputfile')
```

### Usage 
```bash
python3 parse_ipynb.py [PATH_TO_IPYNB]
```
For optional arguments use -h
## run_ipynb
Invokes parse_ipynb to extract sourcecode from ipynb file and runs code afterwards.
#### Usage 
```bash
python3 run_ipynb.py [PATH_TO_IPYNB]
```
For optional arguments use -h

### TODOS
- [ ] also convert to html, pdf
- [ ] add markdown-cell above of code-cell as docstring  
- [ ] automatic multiprocessing (Workpool) of functions in for-loop if multiprocessing argument is enabled  
