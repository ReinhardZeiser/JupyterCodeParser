# JupyterCodeParser
Simple module to extract/run code written in a Jupyter Notebook.  
  
**Usecase:** 
- extracting code after prototyping in Jupyter
- program in Jupyter for better documentations and always run your code with run_ipynb.py 

## parse_ipynb
Parses code from Jupyter file (\*.ipynb) and writes it to outputfile. 
### Usage 
```bash
python3 parse_ipynb.py [PATH_TO_IPYNB]
```
For optional arguments use -h
## run_ipynb
Invokes parse_ipynb and runs extracted code.
#### Usage 
```bash
python3 run_ipynb.py [PATH_TO_IPYNB]
```
For optional arguments use -h

### TODOS
- [ ] if *# omit cell* in first line of code cell, don't add cell to code  
- [ ] add markdown-cell above of code-cell as docstring  
- [ ] automatic multiprocessing (Workpool) of functions in for-loop if multiprocessing argument is enabled  
