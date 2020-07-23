from programs import stringsort
import pytest


def test_1():
    assert stringsort.sortstring("hello again")=="again hello"