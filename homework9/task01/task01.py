"""
Write a function that merges integer from sorted files and returns an iterator
file1.txt:
1
3
5
file2.txt:
2
4
6
>> list(merge_sorted_files(["file1.txt", "file2.txt"]))
[1, 2, 3, 4, 5, 6]
"""
from pathlib import Path
from typing import Iterator, List, Union


def merging_lists(lists):
    result_list = []
    while lists:
        for list in lists:
            if (
                lists.index(list) == 0 and len(list) > 0
            ):  # минимальным принимаю первый элемент вложенного списка
                minimum = list.pop(0)
                result_list.append(minimum)
            for el in list:
                if el >= minimum:
                    break
                else:  # если находится элемент, меньше установленного мимнимума - минимум заменяется
                    lists[0].insert(0, minimum)
                    minimum = list.pop(0)
                    result_list[-1] = minimum
        lists = [
            list for list in lists if list
        ]  # удаляю пустые списки, которые больше не используются
    return result_list


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:
    lists = []
    for file_name in file_list:
        with open(file_name) as numbers:
            sub_list = []
            for line in numbers:
                sub_list.append(int(line.strip("\n")))
            lists.append(sub_list)
    iterator = iter(merging_lists(lists))
    return iterator
