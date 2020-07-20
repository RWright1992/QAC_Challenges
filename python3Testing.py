import pytest
import string_gen

string = string_gen.string_gen()


def test_string():
    assert isinstance(string, str) == True

def test_5_characters():
    assert len(string) <= 5

def test_lowercase():
    assert string.islower() == True