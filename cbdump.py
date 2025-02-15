
# A simple codebase dumper which assembles the contents of any specified file types under any directory as one large string, containing captions/headers for each file.

import os
from typing import Iterable



def get_code_from_file(fpath: str, ignore_errors: bool = False) -> str:
    with open(fpath, 'r') as f:
        try:
            code = f.read()
        except UnicodeDecodeError as e:
            if ignore_errors:
                return f'Could not read file: {e}'
            raise Exception(f'Error reading file {fpath}:\n{e}')
        if code.isspace():
            return 'Empty file'
        return code



def concatenate_code(code_list: list[str], captions: list[str]) -> str:
    return '\n\n'.join(f'{caption}\n\n{code}' for caption, code in zip(captions, code_list))



def dump(directories: list[str], file_types: Iterable[str], caption_prefix: str = 'FILE ', include_full_path: bool = False, ignore_file_read_errors: bool = False) -> str:
    '''
    Dumps the contents of the specified file types under the specified directories as a single string.
    '''
    code = []
    captions = []
    for directory in directories:
        if not include_full_path:
            directory_parent = os.path.dirname(directory)
        for root, _, fnames in os.walk(directory):
            for file in fnames:
                for file_type in file_types:
                    if file.endswith(file_type):
                        break # Include this file
                else:
                    continue # Skip this file
                fpath = os.path.join(root, file)
                code.append(get_code_from_file(fpath, ignore_errors=ignore_file_read_errors))
                # Include name of `directory` but remove the preceding directories if `include_full_path` is True.
                if not include_full_path:
                    fpath = os.path.relpath(fpath, directory_parent)
                captions.append(f'{caption_prefix}{fpath}')
    return concatenate_code(code, captions)



if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Dump the contents of specified codebases (directories) into a single output file."
    )
    parser.add_argument(
        "-o", "--output",
        type=str,
        required=True,
        help="Path to the output file where the dumped code will be written."
    )
    parser.add_argument(
        "-paths",
        type=str,
        required=True,
        help='Comma-separated list of directories to search (e.g. "path/to/codebase1,path/to/codebase2").'
    )
    parser.add_argument(
        "-ftypes",
        type=str,
        required=True,
        help='Comma-separated list of file types to include (e.g. ".py,.js,.php").'
    )
    parser.add_argument(
        "--ignore-file-read-errors",
        action="store_true",
        help="Continue processing even if there are errors reading some files."
    )

    args = parser.parse_args()

    # Split the comma-separated lists and remove any accidental whitespace.
    directories = [p.strip() for p in args.paths.split(",") if p.strip()]
    file_types = [ft.strip() for ft in args.ftypes.split(",") if ft.strip()]

    # Call the dump function with the parsed arguments.
    dumped_code = dump(directories, file_types, ignore_file_read_errors=args.ignore_file_read_errors)

    # Write the output to the specified file.
    with open(args.output, "w") as out_file:
        out_file.write(dumped_code)


