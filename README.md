# codebase_dump
A simple codebase dumper which assembles the contents of all files, given whitelisted file types, under all given directories as one large string, containing captions/headers for each file.

## Example usage
Basic usage:
```python
import codebase_dump as cbdump

dirpaths = ['path/to/codebase1', 'path/to/codebase2']
file_types = ['.py', '.js', '.php']
ignore_file_read_errors = True
caption_prefix = 'FILE '

code = cbdump.dump(dirpaths, file_types, ignore_file_read_errors=ignore_file_read_errors, caption_prefix=caption_prefix)

print(code)
```

Supply program args and output to file:
```ps
python cbdump.py -o ./output.txt -paths "path/to/codebase1","path/to/codebase2" -ftypes .py,.js,.php --ignore-file-read-errors
```
