# codebase_dump
A simple codebase dumper which assembles the contents of any specified file types under any directory as one large string, containing captions/headers for each file.

## Example usage
Basic usage:
```python
from codebase_dump import dump

dirpaths = ['path/to/codebase1', 'path/to/codebase2']
file_types = ['.py', '.js', '.php']

code = dump(dirpaths, file_types)

print(code)
```

Supply program args and output to file:
```ps
python cbdump.py -o ./output.txt -paths "path/to/codebase1","path/to/codebase2" -ftypes .py,.js,.php --ignore-file-read-errors
```
