"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""

import os
from collections import Counter
from typing import List


def get_longest_diverse_words(file_path: str) -> List[str]:
    amount_symbols = []
    with open(os.path.join(file_path)) as text:
        for word in text.read().split():
            amount_symbols.append([word, len(set(word))])
    amount_symbols.sort(key=lambda x: x[1], reverse=True)
    result = []
    for j in range(10):
        result.append(amount_symbols[j][0])
    return result


def get_longest_diverse_words_with_counter(file_path: str) -> List[str]:
    symbols = []
    with open(os.path.join(file_path)) as text:
        for word in text.read().split():
            symbols.append([word, len(Counter(word))])
    symbols.sort(key=lambda x: x[1], reverse=True)
    result_with_counter = []
    for j in range(10):
        result_with_counter.append(symbols[j][0])
    return result_with_counter


def get_rarest_char(file_path: str) -> str:
    characters = {}
    with open(os.path.join(file_path)) as text:
        for word in text.read().split():
            for symbol in word:
                if symbol.lower() not in characters.keys():
                    characters[symbol.lower()] = 1
                else:
                    characters[symbol.lower()] += 1
    result_list = []
    noun = min(characters.values())
    for i in characters.keys():
        if characters[i] == noun:
            result_list.append(i)
    x = ", ".join(result_list)
    return x


def count_punctuation_chars(file_path: str) -> int:
    punctuations = {}
    with open(os.path.join(file_path)) as text:
        for word in text.read().split():
            for symbol in word:
                if not symbol.isalpha():
                    if not symbol.isnumeric():
                        if symbol not in punctuations.keys():
                            punctuations[symbol] = 1
                        else:
                            punctuations[symbol] += 1
    sum_punctuation = 0
    for j in punctuations.values():
        sum_punctuation = sum_punctuation + j
    return sum_punctuation


def count_non_ascii_chars(file_path: str) -> int:
    ascii_char = {}
    with open(os.path.join(file_path)) as text:
        for word in text.read().split():
            for char in word:
                if not char.isascii():
                    if char not in ascii_char.keys():
                        ascii_char[char] = 1
                    else:
                        ascii_char[char] += 1
    sum_ascii_char = 0
    for j in ascii_char.values():
        sum_ascii_char = sum_ascii_char + j
    return sum_ascii_char


def get_most_common_non_ascii_char(file_path: str) -> str:
    most_common_ascii_char = {}
    with open(os.path.join(file_path)) as text:
        for word in text.read().split():
            for ascii_char in word:
                if not ascii_char.isascii():
                    if ascii_char not in most_common_ascii_char.keys():
                        most_common_ascii_char[ascii_char] = 1
                    else:
                        most_common_ascii_char[ascii_char] += 1
    result_list = []
    if len(most_common_ascii_char) == 0:
        return "None"
    noun = min(most_common_ascii_char.values())
    for i in most_common_ascii_char.keys():
        if most_common_ascii_char[i] == noun:
            result_list.append(i)
    non_ascii_char = ", ".join(result_list)
    return non_ascii_char
