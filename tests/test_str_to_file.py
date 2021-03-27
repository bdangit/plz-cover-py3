import os
from pathlib import Path

import pyfakefs
import pytest

from envutil.envutil import envutil


def test_create_file_with_single_line(fs):
    input_val = "this is a single line"
    filepath = "some/place/file"
    expected_val = "this is a single line"

    envutil.str_to_file(input_val, filepath)
    assert Path(filepath).read_text() == expected_val


def test_create_file_with_line_breaks(fs):
    input_val = "this is the first line\nthis is the next line"
    filepath = "some/place/file"
    expected_val = """this is the first line
this is the next line"""

    envutil.str_to_file(input_val, filepath)
    assert Path(filepath).read_text() == expected_val


def test_create_file_with_multilines(fs):
    input_val = """this is the first line
this is the next line"""
    filepath = "some/place/file"
    expected_val = """this is the first line
this is the next line"""

    envutil.str_to_file(input_val, filepath)
    assert Path(filepath).read_text() == expected_val


def test_create_file_with_None(fs):
    input_val = None
    filepath = "some/place/file"
    expected_val = "INVALID: Nothing provided"

    envutil.str_to_file(input_val, filepath)
    assert Path(filepath).read_text() == expected_val
