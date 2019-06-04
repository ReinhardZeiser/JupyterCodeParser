from parse_ipynb import parse as load_ipynb_code
import subprocess
import sys

def run(ipynb_path):
    code_path = load_ipynb_code(ipynb_path)
    subprocess.run(['python', code_path])


if __name__ == '__main__':
    ipynb_path = sys.argv[1]
    run(ipynb_path)
