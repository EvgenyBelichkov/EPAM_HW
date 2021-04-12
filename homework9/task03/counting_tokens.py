"""
Write a function that takes directory path, a file extension and an optional tokenizer.
It will count lines in all files with that extension if there are no tokenizer.
If a the tokenizer is not none, it will count tokens.
For dir with two files from hw1.py:
>> universal_file_counter(test_dir, "txt")
6
>> universal_file_counter(test_dir, "txt", str.split)
6
"""


import os
from pathlib import Path
from typing import Callable, Optional


def collecting_required_files(dir_path, file_extension: str):
    documents = []
    for file in os.listdir(dir_path):
        if file.endswith(file_extension):
            documents.append(os.path.join(dir_path, file))
    return documents


def collecting_data(files):
    data = []
    for file in files:
        with open(file) as i:
            for line in i:
                data.append(line)
    return data


def universal_file_counter(
    dir_path: Path, file_extension: str, tokenizer: Optional[Callable] = None
) -> int:
    result = 0
    files = collecting_required_files(dir_path, file_extension)
    if tokenizer:
        for i in collecting_data(files):
            result += len(tokenizer(i))
        return result
    else:
        return len(collecting_data(files))
