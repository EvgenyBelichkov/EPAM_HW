import os

from homework9.task03.counting_tokens import universal_file_counter


def test_universal_file_counter_function_without_tokenizer():
    assert (
        universal_file_counter(
            os.path.join(os.path.dirname(__file__), "files_for_testing"), ".txt"
        )
        == 9
    )


def test_universal_file_counter_function_with_tokenizer_method_split_txt_file():
    assert (
        universal_file_counter(
            os.path.join(os.path.dirname(__file__), "files_for_testing"),
            ".txt",
            tokenizer=str.split,
        )
        == 18
    )


def test_universal_file_counter_function_with_tokenizer_method_split_myext_file():
    assert (
        universal_file_counter(
            os.path.join(os.path.dirname(__file__), "files_for_testing"),
            ".myext",
            tokenizer=str.split,
        )
        == 7
    )
