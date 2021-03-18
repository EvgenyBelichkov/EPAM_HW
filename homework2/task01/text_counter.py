"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""

import locale
import os
import tokenize
from collections import Counter, defaultdict
from typing import List
from unicodedata import category

loc = locale.getdefaultlocale()
print(loc)


def get_longest_diverse_words(file_path: str) -> List[str]:
    longest_words = []
    with open(os.path.join(file_path)) as text:
        tokens = tokenize.generate_tokens(text.readline)
        for token in tokens:
            if token.type == 1:
                longest_words.append([token.string, len(set(token.string))])
    longest_words.sort(key=lambda x: x[1], reverse=True)
    result = []
    for j in range(10):
        result.append(longest_words[j][0])
    return result


def get_longest_diverse_words_with_counter(file_path: str) -> List[str]:
    symbols = []
    with open(os.path.join(file_path)) as text:
        tokens = tokenize.generate_tokens(text.readline)
        for token in tokens:
            if token.type == 1:
                symbols.append([token.string, len(Counter(token.string))])
    symbols.sort(key=lambda x: x[1], reverse=True)
    result_with_counter = []
    for j in range(10):
        result_with_counter.append(symbols[j][0])
    return result_with_counter


def get_rarest_char(file_path: str) -> str:
    characters = defaultdict(int)
    with open(os.path.join(file_path)) as text:
        tokens = tokenize.generate_tokens(text.readline)
        for token in tokens:
            if (
                token.type == 1
                or token.type == 2
                or token.type == 3
                or token.type == 54
            ):
                for symbol in token.string:
                    characters[symbol.lower()] += 1
    result_list = []
    noun = min(characters.values())
    for i in characters:
        if characters[i] == noun:
            result_list.append(i)
    x = ", ".join(result_list)
    return x


def count_punctuation_chars(file_path: str) -> int:
    haracters = defaultdict(int)
    with open(os.path.join(file_path)) as text:
        tokens = tokenize.generate_tokens(text.readline)
        for token in tokens:
            for symbol in token.string:
                if category(symbol) in ["Po", "Pd", "Pe", "Pf", "Pi", "Po", "Ps"]:
                    haracters[symbol] += 1
    sum_punctuation = 0
    for j in haracters.values():
        sum_punctuation = sum_punctuation + j
    return sum_punctuation


def count_non_ascii_chars(file_path: str) -> int:
    ascii_char = defaultdict(int)
    with open(os.path.join(file_path)) as text:
        tokens = tokenize.generate_tokens(text.readline)
        for token in tokens:
            for symbol in token.string:
                if not symbol.isascii():
                    ascii_char[symbol] += 1
    sum_ascii_char = 0
    for j in ascii_char.values():
        sum_ascii_char = sum_ascii_char + j
    return sum_ascii_char


def get_most_common_non_ascii_char(file_path: str) -> str:
    most_common_ascii_char = defaultdict(int)
    with open(os.path.join(file_path)) as text:
        tokens = tokenize.generate_tokens(text.readline)
        for token in tokens:
            for symbol in token.string:
                if not symbol.isascii():
                    most_common_ascii_char[symbol] += 1
    result_list = []
    if len(most_common_ascii_char) == 0:
        return "None"
    noun = max(most_common_ascii_char.values())
    for i in most_common_ascii_char:
        if most_common_ascii_char[i] == noun:
            result_list.append(i)
    non_ascii_char = ", ".join(result_list)
    return non_ascii_char
