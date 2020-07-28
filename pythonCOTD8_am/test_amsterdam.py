import pytest
import amsterdam

def test_one():
    assert amsterdam.hamsterjams("Am I in Amsterdam")== 1

def test_two():
    assert amsterdam.hamsterjams("I am in Amsterdam am I?")== 2

def test_three():
    assert amsterdam.hamsterjams("I have been in Amsterdam")== 0

def test_four():
    assert amsterdam.hamsterjams("am am am am")== 4

def test_five():
    assert amsterdam.hamsterjams("")== 0


